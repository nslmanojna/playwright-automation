# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'Login to your account' is visible
# 6. Enter the correct email address and password
# 7. Click 'login' button
# 8. Verify that 'Logged in as username' is visible
# 9. Click 'Delete Account' button
# 10. Verify that 'ACCOUNT DELETED!' is visible


import time


def test_login_with_registered_user(page, register_user):
    page, name, email, password = register_user

    if page.locator(f"text=Logged in as {name}").is_visible():
        page.get_by_role("link", name=" Logout").click()
    page.wait_for_load_state("networkidle")
    page.get_by_role("link", name=" Signup / Login").click()
    assert page.locator("text='Login to your account'").is_visible()
    page.locator("//input[@data-qa='login-email']").fill(email)
    page.locator("//input[@data-qa='login-password']").fill(password)
    page.get_by_role("button", name="Login").click()
    assert page.locator(f"text=Logged in as {name}").is_visible()
    print(f"Successfully logged in with Username: {email} and Password: {password}.")


