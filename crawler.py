from playwright.sync_api import sync_playwright
import time
import random
import subprocess

def connect_vpn():
    print("🔌 Connecting to VPN (UK)...")
    subprocess.run(["protonvpn-cli", "c", "--cc", "UK"])
    time.sleep(6)

def disconnect_vpn():
    print("🔌 Disconnecting VPN...")
    subprocess.run(["protonvpn-cli", "d"])

def random_sleep(a=1, b=3):
    time.sleep(random.uniform(a, b))

def slow_type(page, selector, text, delay=0.1):
    page.click(selector)
    for char in text:
        page.keyboard.type(char)
        time.sleep(delay)

def run_scraper():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        try:
            page = browser.new_page()
            page.goto('https://www.adzuna.com/')

            random_sleep(2, 4)
            page.wait_for_selector('header nav ul li:first-child a', state="visible")
            page.click('header nav ul li:first-child a')

            page.wait_for_load_state('domcontentloaded')
            random_sleep(1, 3)

            page.wait_for_selector('#email', state="visible")
            random_sleep(1, 4)
            slow_type(page, '#email', 'kalabiq1@gmail.com', delay=0.15)

            random_sleep(2, 4)
            slow_type(page, '#password', 'A55975597a!', delay=0.2)

            random_sleep(1, 5)
            page.mouse.wheel(0, 300)
            random_sleep(2, 4)

            button = page.query_selector('form button[type="submit"]')
            if button:
                box = button.bounding_box()
                page.mouse.move(box['x'] + box['width']/2, box['y'] + box['height']/2, steps=25)
                random_sleep(1, 2)
                page.get_by_role('button', name='Login').click()
                page.wait_for_load_state('domcontentloaded')
                print("✅ Login complete, waiting to observe page...")
                time.sleep(10)
            else:
                print("❌ Could not find login button.")
        finally:
            browser.close()

if __name__ == "__main__":
    try:
        connect_vpn()
        run_scraper()
    finally:
        disconnect_vpn()
