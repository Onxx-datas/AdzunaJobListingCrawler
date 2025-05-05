import requests

with open("proxy_settings/working_proxies.txt") as file:
    proxies = [line.strip() for line in file if line.strip()]

uk_proxies = []

for proxy in proxies:
    ip = proxy.split(":")[0]
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}?fields=countryCode", timeout=5)
        if res.json().get("countryCode") == "GB":
            print(f"UK Proxy: {proxy}")
            uk_proxies.append(proxy)
    except:
        print(f"Failed to check location for: {proxy}")

with open("proxy_settings/uk_proxies.txt", "w") as out:
    for p in uk_proxies:
        out.write(p + "\n")
