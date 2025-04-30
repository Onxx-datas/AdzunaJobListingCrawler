from playwright.sync_api import sync_playwright
import time
import random

def random_sleep(a=1, b=3):
    time.sleep(random.uniform(a, b))
def slow_type(page, selector, text, delay=0.1):
    page.click(selector)
    for char in text:
        page.keyboard.type(char)
        time.sleep(delay)

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto('https://www.adzuna.com/')
        random_sleep(2, 4)
        page.wait_for_selector('header nav ul li:first-child a', state="visible")
        page.click('header nav ul li:first-child a')
        page.wait_for_load_state('domcontentloaded')
        random_sleep(1, 3)
        page.wait_for_selector('#email', state='visible')
        random_sleep(1, 4)
        slow_type(page, '#email', '', delay=0.15)
        random_sleep(2, 4)
        slow_type(page, '#password', '', delay=0.2)
        random_sleep(1, 5)
        page.mouse.wheel(0, 300)
        random_sleep(2, 4)
        button = page.query_selector('form button[type="submit"]')
        box = button.bounding_box()
        page.mouse.move(box['x'] + box['width']/2, box['y'] + box['height']/2, steps=25)
        random_sleep(1, 2)
        page.get_by_role('button', name='Login').click()
        page.wait_for_load_state('domcontentloaded')
        random_sleep(3, 6)
        page.wait_for_selector('#what', state='visible')
        slow_type(page, '#what', 'Logistics', delay=0.3)
        random_sleep(1, 2)
        page.click('button[type="submit"]')
        random_sleep(3, 5)
        page.wait_for_selector('div.flex.gap-4 h2 a')
        links = page.query_selector_all('div.flex.gap-4 h2 a')
        for link in links:
            text = link.inner_text().strip()
            print(text)
        

        time.sleep(10)
finally:
    browser.close()