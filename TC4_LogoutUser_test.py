# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'Login to your account' is visible
# 6. Enter correct email address and password
# 7. Click 'login' button
# 8. Verify that 'Logged in as username' is visible
# 9. Click 'Logout' button
# 10. Verify that user is navigated to login page

def test_logoutuser(page,register_user):
    page, name, email, password = register_user

    if page.locator(f"text=Logged in as {name}").is_visible():
        page.get_by_role("link", name=" Logout").click()

    page.wait_for_load_state("networkidle")
    assert page.get_by_role("link", name=" Signup / Login").is_visible()
    assert page.url.__contains__("/login")
