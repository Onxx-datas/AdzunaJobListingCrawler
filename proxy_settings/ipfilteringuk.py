import requests

# Load working proxies
with open("proxy_settings/working_proxies.txt") as file:
    proxies = list(set(line.strip() for line in file if line.strip()))

uk_proxies = []

for proxy in proxies:
    ip = proxy.split(":")[0]
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}?fields=status,countryCode,message", timeout=5)
        data = res.json()

        if data.get("status") == "success" and data.get("countryCode") == "GB":
            print(f"[+] UK Proxy: {proxy}")
            uk_proxies.append(proxy)
        else:
            reason = data.get("message", "Not UK")
            print(f"[-] Skipped {proxy} → Reason: {reason}")

    except Exception as e:
        print(f"[!] Failed to check location for: {proxy} → {e}")

# Save UK proxies
with open("proxy_settings/uk_proxies.txt", "w") as out:
    for p in sorted(set(uk_proxies)):
        out.write(p + "\n")

print(f"\n✅ {len(uk_proxies)} UK proxies saved to uk_proxies.txt")
