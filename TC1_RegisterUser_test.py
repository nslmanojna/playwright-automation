# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'New User Signup!' is visible
# 6. Enter name and email address
# 7. Click 'Signup' button
# 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
# 9. Fill details: Title, Name, Email, Password, Date of birth
# 10. Select checkbox 'Sign up for our newsletter!'
# 11. Select checkbox 'Receive special offers from our partners!'
# 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
# 13. Click 'Create Account button'
# 14. Verify that 'ACCOUNT CREATED!' is visible
# 15. Click 'Continue' button
# 16. Verify that 'Logged in as username' is visible
# 17. Click 'Delete Account' button
# 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button


import time


def test_deleteuser(page,register_user):
    page, name, email, password = register_user

    # 17. Click 'Delete Account' button
    if page.locator(f"text=Logged in as {name}").is_visible():
        page.get_by_role("link", name=" Delete Account").click()

    # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    page.wait_for_load_state("networkidle")
    assert page.locator("text='Account Deleted!'").is_visible()
    # 15. Click 'Continue' button
    page.get_by_role("link", name="Continue").click()
    assert page.title().__eq__("Automation Exercise")
    print("User is on Home Page")















