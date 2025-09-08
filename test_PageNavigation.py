from playwright.sync_api import Playwright, expect

def test_pagenaviagtion_GAPortal(playwright: Playwright):
    # Launch browser
    browser = playwright.chromium.launch(headless=False)

    # Create context with video recording
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size= {"width": 1280, "height": 720}
    )
    # Make sure to close context, so that videos are saved.

    # Start page
    page = context.new_page()

    # Navigate to login
    page.goto("https://stggauxweb-us.userexperience.ges.deloitte.com/ga/login")
    page.wait_for_load_state("networkidle")

    # Assertions on page title and welcome text
    expect(page).to_have_title("GlobalAdvantage")
    expect(page.get_by_text("Welcome to GlobalAdvantage.")).to_be_visible()

    # Login
    username = "tus01_12may2025_tu01@ga-testing.com"
    password = "Application@123"
    page.locator("//input[@type='text']").fill(username)
    page.get_by_role("button", name="Continue").click()
    page.locator("//input[@type='password']").fill(password)
    page.get_by_role("button", name="Log In").click()

    # Wait for landing page
    page.wait_for_url("**/ga/portal/landing-page")

    # Extract and verify user name
    text = page.locator("//p").nth(0).inner_text()
    print(text)
    name = text.split(",")[1].strip()
    print(f"Extracted user: {name}")
    expect(page.locator("//p").nth(0)).to_have_text(f"Welcome, {name}")

    # Click Newsfeed
    page.get_by_role("button", name="Newsfeed dropdown").first.click()
    page.get_by_role("button", name="Newsfeed", exact=True).click()
    page.wait_for_selector("//h1")

    # Wrap action that opens new page inside expect_page
    with context.expect_page() as new_page_info:
        page.get_by_role("link", name="Read more").click()
    new_page = new_page_info.value
    new_page.wait_for_load_state("domcontentloaded")

    print(new_page.title())
    assert "Deloitte Global" in new_page.title()

    print("Test Completed")

    # Close context to save video
    context.close()
    browser.close()


