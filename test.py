# from playwright.sync_api import sync_playwright
# import time
# import random

# def random_sleep(a=1, b=3):
#     time.sleep(random.uniform(a, b))

# try:
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=50)
#         page = browser.new_page()
#         page.goto('https://www.adzuna.com/')
#         random_sleep(2, 4)

#         # Login process
#         page.click('header nav ul li:first-child a')
#         page.wait_for_selector('#email')
#         random_sleep(1, 2)
#         page.fill('#email', 'kalabiq1@gmail.com')  # Fill your email
#         random_sleep(1, 2)
#         page.fill('#password', 'your_password_here')  # Fill your password
#         page.get_by_role('button', name='Login').click()
#         page.wait_for_load_state('domcontentloaded')
#         random_sleep(3, 5)

#         # Search for 'Logistics'
#         page.fill('#what', 'Logistics')
#         page.click('button[type="submit"]')
#         random_sleep(3, 5)

#         # Click first job title
#         page.wait_for_selector('div.flex.gap-4 h2 a')
#         first_link = page.query_selector('div.flex.gap-4 h2 a')
#         if first_link:
#             print("Clicking first job title...")
#             first_link.click()
#             time.sleep(10)  # Wait to see the result
#         else:
#             print("No job links found.")

# finally:
#     browser.close()
