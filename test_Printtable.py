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
from playwright.sync_api import sync_playwright, Playwright
from tabulate import tabulate


def test_AddProducts_Cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        page.goto("http://automationexercise.com")
        page.wait_for_load_state("networkidle")

        # 3. Verify that home page is visible successfully
        assert page.title() == "Automation Exercise"

        # 4. Click 'Products' button
        page.get_by_role("link", name="Products").click()
        page.wait_for_load_state("networkidle")

        # 5. Hover over first product and click 'Add to cart'
        assert page.locator("text='All Products'").is_visible()
        page.mouse.wheel(0, 500)

        firstproduct = page.locator("//div[@class='product-image-wrapper']").filter(has_text="Blue Top")
        firstproduct.hover()
        firstproduct.locator("a[data-product-id='1']").first.click()

        # 6. Click 'Continue Shopping' button
        cartmodal = page.locator("div.modal-content")
        cartmodal.get_by_role("button", name="Continue Shopping").click()
        time.sleep(2)

        # 7. Hover over second product and click 'Add to cart'
        secondproduct = page.locator("//div[@class='product-image-wrapper']").filter(has_text="Men Tshirt")
        secondproduct.hover()
        secondproduct.locator("a[data-product-id='2']").first.click()
        time.sleep(2)

        # 8. Click 'View Cart' button
        cartmodal.get_by_role("link", name="View Cart").click()
        page.wait_for_load_state("networkidle")

        # 9. Verify both products are added to Cart
        product1 = page.locator("//a[@href='/product_details/1']").inner_text()
        product2 = page.locator("//a[@href='/product_details/2']").inner_text()
        assert product1 == "Blue Top"
        assert product2 == "Men Tshirt"

        # 10. Verify their prices, quantity and total price
        page.wait_for_selector("#cart_info_table")

        # Get rows and column headers
        rows = page.locator("//tbody //tr")
        row_count = rows.count()
        columns=page.locator("thead tr td")
        col_count=columns.count()

        # Extract headers
        headers = [columns.nth(j).inner_text() for j in range(col_count) if columns.nth(j).inner_text() != ""]

        # Store table data
        table_data = []

        for i in range(row_count):
            row_values = []
            for j in range(col_count):
                header = columns.nth(j).inner_text()
                if header == "Item":
                    row_values.append(f"Product{i + 1}")
                elif header != "":
                    value = page.locator(f"//tbody//tr/td[{j + 1}]").nth(i).inner_text()
                    row_values.append(value)
            table_data.append(row_values)

        # Print as table
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

        context.close()
        browser.close()


        #
        # for i in range(row_count):
        #     row = rows.nth(i)
        #     for j in range(col_count):
        #         col = columns.nth(j)
        #         header=col.inner_text()
        #         if header=="Item":
        #             #value=page.locator("//tbody//tr/td[1]").inner_text()
        #             print(f"{header}: Product{i}")
        #         if header == "Description":
        #             value = page.locator("//tbody//tr/td[2]").nth(i).inner_text()
        #             print(f"{header}:{value}")
        #         if header=="Price":
        #             value=page.locator("//tbody//tr/td[3]").nth(i).inner_text()
        #             print(f"{header}:{value}")
        #         if header=="Quantity":
        #             value=page.locator("//tbody//tr/td[4]").nth(i).inner_text()
        #             print(f"{header}:{value}")
        #         if header=="Total":
        #             value=page.locator("//tbody//tr/td[5]").nth(i).inner_text()
        #             print(f"{header}:{value}")
        #         if header=="":
        #             break
