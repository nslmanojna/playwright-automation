import os
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def test_uploadFile_DialogAccept(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 1280, "height": 720}
    )
    page = context.new_page()
    page.goto("https://automationexercise.com/")

    # Create a sample file if not already present
    os.makedirs("files", exist_ok=True)
    filepath1 = os.path.join(os.getcwd(), "files", "PythonText.txt")
    filepath2 = os.path.join(os.getcwd(), "files", "python.txt")
    uploadfiles= [filepath1,filepath2]
    if not os.path.exists(filepath1):
        with open(filepath1, "w") as f:
            f.write("This is a sample file for Playwright upload test.")

    print("File path for upload:", filepath1)

    # Navigate to Contact Us page
    page.get_by_role("link", name=" Contact us").click()
    page.wait_for_load_state("networkidle")

    # Assert the contact page is loaded
    expect(page.locator("text='Get In Touch'")).to_be_visible()

    # Fill the form
    page.get_by_placeholder("Name").fill("Testuser")
    page.locator("//input[@data-qa='email']").fill("testuser1@mailinator.com")
    page.get_by_placeholder("Subject").fill("Testing")
    page.get_by_placeholder("Your Message Here").fill("Playwright testing")

    # Upload the file
    page.set_input_files("input[type='file']", filepath1)

    # Upload multiple files
    # page.set_input_files("input[type='file']", uploadfiles)

    # Attach dialog handler BEFORE clicking submit
    page.once("dialog", lambda dialog: dialog.accept())

    # Submit the form
    page.get_by_role("button", name="Submit").click()

    # Check for the success message
    expect(page.locator("//div[@class='status alert alert-success']")).to_be_visible()

    # Click on 'Home' and verify page title
    #page.get_by_role("link", name="Home").click()
    page.click("//a[@class='btn btn-success']")
    expect(page).to_have_title("Automation Exercise")

    context.close()
    browser.close()

def test_uploadFile_DialogDecline(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 1280, "height": 720}
    )
    page = context.new_page()
    page.goto("https://automationexercise.com/")

    # Create a sample file if not already present
    filepath = os.path.join(os.getcwd(), "files", "PythonText.txt")
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            f.write("This is a sample file for Playwright upload test.")

    print("File path for upload:", filepath)

    # Navigate to Contact Us page
    page.get_by_role("link", name=" Contact us").click()
    page.wait_for_load_state("networkidle")

    # Assert the contact page is loaded
    expect(page.locator("text='Get In Touch'")).to_be_visible()

    # Fill the form
    page.get_by_placeholder("Name").fill("Testuser")
    page.locator("//input[@data-qa='email']").fill("testuser1@mailinator.com")
    page.get_by_placeholder("Subject").fill("Testing")
    page.get_by_placeholder("Your Message Here").fill("Playwright testing")

    # Upload the file
    page.set_input_files("input[type='file']", filepath)

    # Attach dialog handler BEFORE clicking submit
    page.once("dialog", lambda dialog: dialog.dismiss())

    # Submit the form
    page.get_by_role("button", name="Submit").click()

    # Check the control is on the same page
    expect(page.locator("text='Get In Touch'")).to_be_visible()
    page.wait_for_timeout(5000)

    context.close()
    browser.close()
