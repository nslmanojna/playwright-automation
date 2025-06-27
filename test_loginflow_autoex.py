# Test Case 2: Login User with correct email and password
# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'Login to your account' is visible
# 6. Enter correct email address and password
# 7. Click 'login' button
# 8. Verify that 'Logged in as username' is visible
# 9. Click 'Delete Account' button
# 10. Verify that 'ACCOUNT DELETED!' is visible

# Import necessary libraries

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False
    )  # Set headless=True to run in the background 
    page = browser.new_page() #Launch browser
    page.goto("https://www.automationexercise.com/") #Navigate to url 'http://automationexercise.com'
    page.wait_for_timeout(5000) #Wait for 2 seconds
    print("Page URL:", page.url) #Get page URL
    print("Page URL:", page.url == "https://www.automationexercise.com/")
    page.click("a[href='/login']")#Click on 'Signup / Login' button
    print("Page Title:", page.title())
    print("Page Title:", page.title()=="Automation Exercise - Signup / Login")
    page.wait_for_timeout(2000) #Wait for 2 seconds
    if page.locator("text=Login to your account").is_visible():#Verify 'New User Signup!' is visible
        print("✅'Login to your account' text is present on the page.")
    page.locator('//input[@data-qa="login-email"]').fill("testuser971@example.com") #Enter email address
    page.locator('//input[@data-qa="login-password"]').fill("Test@123") #Enter password
    page.click("button[data-qa='login-button']") #Click 'Login' button
    if page.locator('text=Logged in as TestUser1').is_visible():#Verify that 'Logged in as 'username' is visible
        print("✅ 'Logged in as TestUser1' text is present on the page.")
    page.click('a[href="/delete_account"]') #Click 'Delete Account' button
    page.wait_for_timeout(2000) #Wait for 2 seconds
    if page.locator('text=Account Deleted!').is_visible():#Verify that 'ACCOUNT DELETED!' is visible
        print("✅ 'Account Deleted!' text is present on the page.") 
    page.click('//a[@data-qa="continue-button"]') #Click 'Continue' button
    page.wait_for_timeout(2000) #Wait for 2 seconds
    if page.locator('//a[@href="/login"]').is_visible():#Verify that 'You have successfully logged out' is visible
        print("✅ 'You are on Home page")
    browser.close()
    print("Browser closed successfully.")
    print("Test completed successfully.")