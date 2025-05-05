import requests
from concurrent.futures import ThreadPoolExecutor

with open("proxies.txt") as file:
    proxies = [line.strip() for line in file if line.strip()]

working_proxies = []

def check_proxy(proxy):
    try:
        response = requests.get(
            "http://httpbin.org/ip",
            proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"},
            timeout=5
        )
        if response.status_code == 200:
            print(f"[+] WORKING: {proxy}")
            working_proxies.append(proxy)
        else:
            print(f"[-] BAD: {proxy}")
    except:
        print(f"[-] DEAD: {proxy}")
with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(check_proxy, proxies)
with open("working_proxies.txt", "w") as out:
    for proxy in working_proxies:
        out.write(proxy + "\n")

print(f"\nDone. {len(working_proxies)} working proxies saved.")
