# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'Login to your account' is visible
# 6. Enter incorrect email address and password
# 7. Click 'login' button
# 8. Verify error 'Your email or password is incorrect!' is visible


import time


def test_login_with_invaliduser(page):
    page.goto("https://automationexercise.com/")
    page.wait_for_load_state("networkidle")
    page.get_by_role("link", name=" Signup / Login").click()
    assert page.locator("text='Login to your account'").is_visible()
    # 6. Enter incorrect email address and password
    invalidemail="testuser@gmail"
    invalidpassword="password@12"
    page.locator("//input[@data-qa='login-email']").fill(invalidemail)
    page.locator("//input[@data-qa='login-password']").fill(invalidpassword)
    # 7. Click 'login' button
    page.get_by_role("button", name="Login").click()
    time.sleep(3)
    # 8. Verify error 'Your email or password is incorrect!' is visible
    assert page.locator("text='Your email or password is incorrect!'")
    time.sleep(3)
    print("User is on Signup/Login Page")
