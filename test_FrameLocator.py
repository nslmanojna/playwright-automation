import time

from playwright.sync_api import Playwright, expect


def test_FrameLocator(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    # Create context with video recording
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.w3schools.com/html/html_iframe.asp")
    page.wait_for_load_state("networkidle")

    # Save the screenshot in that folder
    page.screenshot(path="screenshots/screenshot.png")

    expect(page.locator("text='Iframes'")).to_have_text("Iframes")
    pageframe = page.frame_locator("//iframe[@title='W3Schools HTML Tutorial']")
    pageframe.get_by_role("link", name='PYTHON', exact=True).click()
    expect(pageframe.locator(".with-bookmark")).to_contain_text("Python ")
    time.sleep(5)

