# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Contact Us' button
# 5. Verify 'GET IN TOUCH' is visible
# 6. Enter name, email, subject and message
# 7. Upload file
# 8. Click 'Submit' button
# 9. Click OK button
# 10. Verify success message 'Success! Your details have been submitted successfully.'
# Is visible
# 11. Click the 'Home' button and verify that user landed on homepage successfully

def test_contactus_form(page):
    page.goto("https://automationexercise.com/")
    page.wait_for_load_state("networkidle")
    assert page.title() == "Automation Exercise"
    page.get_by_role("link", name=" Contact us").click()
    page.wait_for_load_state("networkidle")
    assert page.locator("text='Get In Touch'").is_visible()
    # 6. Enter name, email, subject and message
    page.get_by_placeholder("Name").fill("Testuser")
    page.locator("//input[@data-qa='email']").fill("testuser1@mailinator.com")
    page.get_by_placeholder("Subject").fill("Testing")
    page.get_by_placeholder("Your Message Here").fill("I learnt playwright testing")
    page.locator("//input[@name='upload_file']").click()

    # Locate the file input and set the file to upload
    page.set_input_files("input[type='file']", "Python.txt")

    # Optionally click the submit button
    page.click("button[type='submit']")  # Adjust selector as needed
    # Handle the alert if it appears on upload
    # Attach dialog handler before the action that triggers the alert
    page.once("dialog", lambda dialog: dialog.accept())
    # 10. Verify success message 'Success! Your details have been submitted successfully.'
    # Is visible
    page.locator("text='Success! Your details have been submitted successfully.'")
    page.locator("text='Home'").click()
    assert page.title()=="Automation Exercise"
