# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Test Cases' button
# 5. Verify user is navigated to test cases page successfully

def test_navigate_TCsPage(page):
    page.goto("https://automationexercise.com/")
    page.title().__eq__("Automation Exercise")

    page.wait_for_load_state("networkidle")

    #page.get_by_role("link", name="Test cases").click()

    page.locator("header[id='header'] li:nth-child(5)").click()
    page.wait_for_load_state("networkidle")
    assert page.title().__contains__("Test Cases")