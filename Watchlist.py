from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://www.amazon.in/")
    page.locator('//input[@placeholder="Search Amazon.in"]').fill("mobile")
    page.locator('//input[@value="Go"]').click()
    #page.get_by_role("link", name = "Apply the filter Samsung to narrow results").click()
    page.get_by_text("All Discounts").click()
    #page.wait_for_selector(2000)
    #page.get_by_role("link",name="Redmi A4 5G (Sparkle Purple, 4GB RAM, 128GB Storage) | Segment Largest 6.88in 120Hz | 50MP Dual Camera | 18W Fast Charging | Charger in The Box").click()
    #page.get_by_role("link",name="submit.add-to-cart").click()
    page.wait_for_timeout(3000)