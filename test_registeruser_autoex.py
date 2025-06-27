#Test Case 1: Register User
#1. Launch browser
#2. Navigate to url 'http://automationexercise.com'
#3. Verify that home page is visible successfully
#4. Click on 'Signup / Login' button
#5. Verify 'New User Signup!' is visible
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
    print("Page Title:", page.title())# Get page title
    print("Page Title:", page.title() =="Automation Exercise")#Verify that home page is visible successfully
    page.click("a[href='/login']")#Click on 'Signup / Login' button
    print("Page Title:", page.title())
    print("Page Title:", page.title()=="Automation Exercise - Signup / Login")
    page.wait_for_timeout(2000) #Wait for 2 seconds
    if page.locator("text=New User Signup!").is_visible():#Verify 'New User Signup!' is visible
        print("✅ 'New User Signup!' text is present on the page.")
    page.locator('//input[@data-qa="signup-name"]').fill("TestUser7") #Enter name
    page.locator('//input[@data-qa="signup-email"]').fill("testuser977@example.com") #Enter email address
    page.click("button[data-qa='signup-button']") #Click 'Signup' button
    page.wait_for_timeout(2000) #Wait for 2 seconds
    if page.locator('text=Enter Account Information').is_visible():#Verify that 'ENTER ACCOUNT INFORMATION' is visible
        print("✅ 'Enter Account Information' text is present on the page.")
    print("Page Title:", page.title())
    #Fill details: Title, Name, Email, Password, Date of birth 
    page.locator('//input[@id="id_gender1"]').check() #Select title 'Mr'
    page.locator('//input[@id="name"]').__eq__("TestUser7") #Name should be filled automatically
    page.locator('//input[@id="email"]').__eq__("testuser977@example.com") #Email should be filled automatically
    page.locator('//input[@id="password"]').fill("Test@123") #Fill password
    page.locator('//select[@id="days"]').select_option("15") #Select day
    page.locator('//select[@id="months"]').select_option(label="June") #Select month by label
    page.locator('//select[@id="years"]').select_option("2020") #Select year
    page.locator('//input[@id="newsletter"]').check() #Select 'Sign up for our newsletter!' checkbox
    page.locator('//input[@id="optin"]').check() #Select 'Receive special offers from our partners!' checkbox
    if page.locator('text=Address Information').is_visible():#Verify that 'Address Information' is visible
        print("✅ 'Address Information' text is present on the page.")
    #Fill details: First Name, Last Name, Company, Address, Country, State, City, Zipcode, Mobile Number
    page.locator('//input[@id="first_name"]').fill("Test") #Fill first name
    page.locator('//input[@id="last_name"]').fill("User7") #Fill last name
    page.locator('//input[@id="company"]').fill("Test Company") #Fill company
    page.locator('//input[@id="address1"]').fill("123 Test St") #Fill address
    page.locator('//input[@id="address2"]').fill("Apt 456") #Fill address line 2
    page.locator('//select[@id="country"]').select_option(label="United States") #Select country by label
    page.locator('//input[@id="state"]').fill("California") #Fill state
    page.locator('//input[@id="city"]').fill("Los Angeles") #Fill city
    page.locator('//input[@id="zipcode"]').fill("90001") #Fill zipcode
    page.locator('//input[@id="mobile_number"]').fill("1234567890") #Fill mobile number    
    page.click('button[data-qa="create-account"]') #Click 'Create Account button'
    page.wait_for_timeout(2000) #Wait for 2 seconds
    if page.locator('text=Account Created!').is_visible():#Verify that 'ACCOUNT CREATED!' is visible
        print("✅ 'Account Created!' text is present on the page.")
    page.click('//a[@data-qa="continue-button"]') #Click 'Continue' button
    page.wait_for_timeout(2000) #Wait for 2 seconds
    if page.locator('text=Logged in as TestUser7').is_visible():#Verify that 'Logged in as 'username' is visible
        print("✅ 'Logged in as TestUser7' text is present on the page.")
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