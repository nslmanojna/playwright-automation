# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Products' button
# 5. Verify user is navigated to ALL PRODUCTS page successfully
# 6. Enter product name in search input and click search button
# 7. Verify 'SEARCHED PRODUCTS' is visible
# 8. Verify all the products related to search are visible


import time


def test_searchproducts(page):# 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    page.goto("https://www.automationexercise.com/")
    # 3. Verify that home page is visible successfully
    assert page.title().__eq__("Automation Exercise")
    # 4. Click on 'Products' button
    page.get_by_role("link", name="Products").click()
    page.wait_for_load_state("networkidle")
    # 5. Verify user is navigated to ALL PRODUCTS page successfully
    assert page.title().__contains__("All Products")
    # 6. Enter product name in search input and click search button
    page.get_by_placeholder("Search Product").fill("jeans")
    page.locator("#submit_search").click()
    page.mouse.wheel(0,700)
    # 7. Verify 'SEARCHED PRODUCTS' is visible
    assert page.locator("text='Searched Products'").is_visible()
    # 8. Verify all the products related to search are visible
    assert page.locator(".product-image-wrapper") != 0
    time.sleep(2)