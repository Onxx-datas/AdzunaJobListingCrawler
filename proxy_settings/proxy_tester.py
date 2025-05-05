import requests
from concurrent.futures import ThreadPoolExecutor

with open("proxy_settings/proxies.txt") as file:
    proxies = [line.strip() for line in file if line.strip()]

working_proxies = []

def check_proxy(proxy):
    try:
        response = requests.get(
            "http://httpbin.org/ip",
            proxies={
                "http": f"http://{proxy}",
                "https": f"http://{proxy}"
            },
            timeout=5
        )
        if response.status_code == 200:
            ip = response.json().get("origin", "")
            print(f"[+] WORKING: {proxy} → Reported IP: {ip}")
            working_proxies.append(proxy)
        else:
            print(f"[-] BAD RESPONSE: {proxy}")
    except Exception:
        print(f"[-] DEAD: {proxy}")

with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(check_proxy, proxies)

working_proxies = list(set(working_proxies))

with open("proxy_settings/working_proxies.txt", "w") as out:
    for proxy in working_proxies:
        out.write(proxy + "\n")

print(f"\nChecked {len(proxies)} proxies.")
print(f"{len(working_proxies)} working proxies saved to working_proxies.txt.")
