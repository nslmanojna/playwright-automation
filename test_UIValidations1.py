import time

from playwright.sync_api import expect


def test_PlaywrightShortcut(page):
    page.goto("https://automationexercise.com/")
    page.get_by_role("link", name='Signup / Login').click()
    page.get_by_text("Login to your account").is_visible()
    page.locator("//input[@data-qa='login-email']").fill("Testuser1@mailinator.com")
    page.get_by_placeholder("Password").fill("Password@123")
    page.get_by_role("button", name='Login').click()
    page.get_by_role("link", name=' Products').click()
    assert page.locator("text='All Products'").is_visible()
    page.mouse.wheel(0,500)
    firstproduct=page.locator(".product-image-wrapper").filter(has_text='Men Tshirt')
    firstproduct.hover()
    firstproduct.get_by_text("Add to cart").first.click()
    cartmodel = page.locator(".modal-content")
    cartmodel.get_by_role("button").click()
    secondproduct = page.locator(".product-image-wrapper").filter(has_text='Winter Top')
    secondproduct.hover()
    secondproduct.get_by_text("Add to cart").nth(0).click()
    cartmodel.get_by_role("link").click()
    expect(page.locator(".cart_product")).to_have_count(2)
    time.sleep(5)

