# Test Case 11: Verify Subscription in Cart page
# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click 'Cart' button
# 5. Scroll down to footer
# 6. Verify text 'SUBSCRIPTION'
# 7. Enter email address in input and click arrow button
# 8. Verify success message 'You have been successfully subscribed!' is visible

import time


def test_subscription_Cartpage(page): # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    page.goto("https://www.automationexercise.com/")
    # 3. Verify that home page is visible successfully
    assert page.title().__eq__("Automation Exercise")
    # 4. Click 'Cart' button
    page.get_by_role("link", name="Cart").click()
    page.wait_for_load_state("networkidle")
    # 5. Scroll down to footer
    page.keyboard.press("End")
    # 6. Verify text 'SUBSCRIPTION'
    assert page.locator("text='Subscription'").is_visible()
    # 7. Enter email address in input and click arrow button
    page.locator("#susbscribe_email").fill("testuser97@mailinator.com")
    page.locator("#subscribe").click()
    # 8. Verify success message 'You have been successfully subscribed!' is visible
    assert page.locator("text='You have been successfully subscribed!'").is_visible()
    time.sleep(3)