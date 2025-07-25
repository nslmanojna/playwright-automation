# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Products' button
# 5. Verify user is navigated to ALL PRODUCTS page successfully
# 6. The product list is visible
# 7. Click on 'View Product' of first product
# 8. User is landed to product detail page
# 9. Verify that product detail is visible: product (name, category,
# price, availability, condition, brand)


def test_verifyallproducts(page):# 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    page.goto("https://www.automationexercise.com/")
    # 3. Verify that home page is visible successfully
    assert page.title().__eq__("Automation Exercise")
    # 4. Click on 'Products' button
    page.get_by_role("link", name="Products").click()
    page.wait_for_load_state("networkidle")
    # 5. Verify user is navigated to ALL PRODUCTS page successfully
    assert page.title().__contains__("All Products")
    # 6. The products list is visible
    page.mouse.wheel(0,500) #Scrolls the page upto 500 pixel
    assert page.locator("text='All Products'").is_visible()
    # 7. Click on 'View Product' of first product
    firstproduct = page.locator("//div[@class='product-image-wrapper']").filter(has_text="Blue Top")
    firstproduct.get_by_role("link").click()
    page.wait_for_load_state("networkidle")
    # 8. User is landed to product detail page
    assert page.title().__contains__("Product Details")
    # 9. Verify that product detail is visible: product (name, category,
    # price, availability, condition, brand)
    productdetails= page.locator(".product-information")
    assert productdetails.locator("text='Blue Top'").is_visible()
    assert productdetails.locator("text='Category: Women > Tops'").is_visible()
    assert productdetails.locator("text='Rs. 500'").is_visible()
    assert productdetails.locator("text='Availability:'").is_visible()
    assert productdetails.locator("text='Condition:'").is_visible()
    assert productdetails.locator("text='Brand:'").is_visible()



