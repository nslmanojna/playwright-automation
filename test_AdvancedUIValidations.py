import os
import time

from playwright.sync_api import Playwright, expect


def test_moreUIValidations(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    # Create context with video recording
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 1280, "height": 720}
    )
    page = context.new_page()
    page.goto("https://automationexercise.com/")


    # Create the screenshots folder if it doesn't exist
    os.makedirs("screenshots", exist_ok=True)

    # Save the screenshot in that folder
    page.screenshot(path="screenshots/screenshot.png")
    page.get_by_role("link", name=" Contact us").click()
    page.wait_for_load_state("networkidle")
    assert page.locator("text='Get In Touch'").is_visible()
    # 6. Enter name, email, subject and message
    page.get_by_placeholder("Name").fill("Testuser")
    page.locator("//input[@data-qa='email']").fill("testuser1@mailinator.com")
    page.get_by_placeholder("Subject").fill("Testing")
    page.get_by_placeholder("Your Message Here").fill("Playwright testing")
    #page.locator("//input[@name='upload_file']").set_input_files('PythonText.txt')
    page.mouse.wheel(0,250)
    page.locator("//input[@name='upload_file']").click()

    # Locate the file input and set the file to upload

    page.set_input_files("input[type='file']", "PythonText.txt")

    # Optionally click the submit button
    #page.get_by_role("button", name='submit').click()
    page.locator("//input[@name='submit']").click()
    page.wait_for_event("dialog")
    # Handle the alert if it appears on upload
    # Attach dialog handler before the action that triggers the alert
    # page.on("dialog", lambda dialog: dialog.dismiss())
    # time.sleep(3)
    page.once("dialog", lambda dialog: dialog.accept())
    # 10. Verify success message 'Success! Your details have been submitted successfully.'
    # Is visible
    expect(page.locator("text='Success! Your details have been submitted successfully.'")).to_be_visible()
    page.locator("text='Home'").click()
    assert page.title() == "Automation Exercise"
    context.close()
    browser.close()


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
    page.get_by_placeholder("Your Message Here").fill("I learn playwright testing")
    page.locator("//input[@name='upload_file']").click()

    # Locate the file input and set the file to upload
    page.set_input_files("input[type='file']", "Playwright/PythonText.txt")

    # Optionally click the submit button
    page.click("button[type='submit']")  # Adjust selector as needed
    time.sleep(5)
    # Handle the alert if it appears on upload
    # Attach dialog handler before the action that triggers the alert
    #page.on("dialog", lambda dialog: dialog.dismiss())
    time.sleep(3)
    page.once("dialog", lambda dialog: dialog.accept())
    # 10. Verify success message 'Success! Your details have been submitted successfully.'
    # Is visible
    assert page.locator(".status.alert.alert-success").is_visible()
    page.locator("text='Home'").click()
    assert page.title()=="Automation Exercise"




