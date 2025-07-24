# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'New User Signup!' is visible
# 6. Enter name and already registered email address
# 7. Click 'Signup' button
# 8. Verify error 'Email Address already exist!' is visible

def test_registeruser_with_existingemail(page,register_user):
    page, name, email, password = register_user

    if page.locator(f"text=Logged in as {name}").is_visible():
        page.get_by_role("link", name=" Logout").click()

    page.wait_for_load_state("networkidle")
    assert page.url.__contains__("/login")

    page.get_by_role("link", name=" Signup / Login").click()
    assert page.get_by_text("New User Signup!").is_visible()

    page.get_by_placeholder("Name").fill(name)
    page.locator("//input[@data-qa='signup-email']").fill(email)
    page.get_by_role("button", name="Signup").click()
    assert page.locator("text='Email Address already exist!'").is_visible()



