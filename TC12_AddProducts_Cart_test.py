# Test Case 12: Add Products in Cart
# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click 'Products' button
# 5. Hover over first product and click 'Add to cart'
# 6. Click 'Continue Shopping' button
# 7. Hover over second product and click 'Add to cart'
# 8. Click 'View Cart' button
# 9. Verify both products are added to Cart
# 10. Verify their prices, quantity and total price


import time

from playwright.sync_api import expect


def test_AddProducts_Cart(page):# 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    page.goto("http://automationexercise.com")
    # 3. Verify that home page is visible successfully
    assert page.title().__eq__("Automation Exercise")
    # 4. Click 'Products' button
    page.get_by_role("link", name="Products").click()
    page.wait_for_load_state("networkidle")
    # 5. Hover over first product and click 'Add to cart'
    assert page.locator("text='All Products'").is_visible()
    page.mouse.wheel(0,500)
    # Locate the first product with "Blue Top"
    firstproduct = page.locator("//div[@class='product-image-wrapper']").filter(has_text="Blue Top")
    # 5. Hover over first product and click 'Add to cart'
    firstproduct.hover()
    firstproduct.locator("(//a[@data-product-id='1'])[1]").click()
    time.sleep(3)
    # 6. Click 'Continue Shopping' button
    cartmodel=page.locator(".modal-content")
    cartmodel.get_by_role("button").click()
    # 7. Hover over second product and click 'Add to cart'
    secondproduct = page.locator("//div[@class='product-image-wrapper']").filter(has_text="Men Tshirt")
    secondproduct.hover()
    secondproduct.locator("(//a[@data-product-id='2'])[1]").click()
    time.sleep(3)
    # 8. Click 'View Cart' button
    cartmodel.get_by_role("link").click()
    time.sleep(5)
    # 9. Verify both products are added to Cart
    product1 = page.locator("//a[@href='/product_details/1']").text_content()
    product2 = page.locator("//a[@href='/product_details/2']").text_content()
    assert  product1 == "Blue Top"
    assert  product2 == "Men Tshirt"
    # 10. Verify their prices, quantity and total price












