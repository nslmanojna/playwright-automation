# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Scroll down to footer
# 5. Verify text 'SUBSCRIPTION'
# 6. Enter email address in input and click arrow button
# 7. Verify success message 'You have been successfully subscribed!' is visible

import  time


def test_subscription_Homepage(page): # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    page.goto("https://www.automationexercise.com/")
    # 3. Verify that home page is visible successfully
    assert page.title().__eq__("Automation Exercise")
    # 4. Scroll down to footer
    page.keyboard.press("End")
    # 5. Verify text 'SUBSCRIPTION'
    assert page.locator("text='Subscription'").is_visible()
    # 6. Enter email address in input and click arrow button
    page.locator("#susbscribe_email").fill("testuser97@mailinator.com")
    page.locator("#subscribe").click()
    # 7. Verify success message 'You have been successfully subscribed!' is visible
    assert page.locator("text='You have been successfully subscribed!'").is_visible()
    time.sleep(2)
