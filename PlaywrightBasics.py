import time

from playwright.sync_api import Playwright, expect


def test_PlaywrightBasics(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://automationexercise.com/")


def test_PlaywrightShortcut(page):
    page.goto("https://automationexercise.com/")
    page.get_by_role("link", name='Signup / Login').click()
    page.get_by_text("Login to your account").is_visible()
    page.locator("//input[@data-qa='login-email']").fill("Testuser1@mailinator.com")
    page.get_by_placeholder("Password").fill("Password@12")
    page.get_by_role("button", name='Login').click()
    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()

def test_FireboxBrowserTest(playwright: Playwright):
    firefoxbrowser= playwright.firefox.launch(headless=False)
    context= firefoxbrowser.new_context()
    page= context.new_page()
    page.goto("https://automationexercise.com/")
    page.get_by_role("link", name='Signup / Login').click()
    page.get_by_text("Login to your account").is_visible()
    page.locator("//input[@data-qa='login-email']").fill("Testuser1@mailinator.com")
    page.get_by_placeholder("Password").fill("Password@12")
    page.get_by_role("button", name='Login').click()
    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()

