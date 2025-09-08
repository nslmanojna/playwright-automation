import random
import time

import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.fixture(scope="session")
def generate_unique_name():
    mynumber = random.randrange(1, 100)
    firstname = "Testuser"
    lastname = mynumber
    name = f"{firstname}_{lastname}"
    return name

@pytest.fixture(scope="session")
def generate_unique_email():
    prefix = "testuser"
    mynumber = random.randrange(1, 100)
    suffix = "@mailinator.com"
    email = f"{prefix}{mynumber}{suffix}"
    return email

@pytest.fixture
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(viewport=None)
        page = context.new_page()
        yield page
        browser.close()
        print("Browser Closed Successfully")
        print("Test completed successfully")

@pytest.fixture
def register_user(page, generate_unique_name, generate_unique_email):
    name = generate_unique_name()
    email = generate_unique_email()
    password = "Password@123"

    #return {"name": name, "email": email, "password": password}

    page.goto("https://automationexercise.com/")
    page.wait_for_load_state("networkidle")

    #assert page.title() == "Automation Exercise"
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name=" Signup / Login").click()
    assert page.get_by_text("New User Signup!").is_visible()

    page.get_by_placeholder("Name").fill(name)
    page.locator("//input[@data-qa='signup-email']").fill(email)
    page.get_by_role("button", name="Signup").click()
    time.sleep(2)

    assert page.title().__contains__("Automation Exercise")
    assert page.locator("text='Enter Account Information'").is_visible()

    page.locator("#id_gender1").check()

    expect("#name").to_contain_text(name)
    expect("#email").to_contain_text(name)
    # assert page.locator("#name").input_value() == name
    # assert page.locator("#email").input_value() == email
    page.get_by_label("Password *").fill(password)

    page.locator("#days").select_option("30")
    page.locator("#months").select_option("August")
    page.locator("#years").select_option("1990")

    page.locator("#newsletter").check()
    page.locator("//input[@name='optin']").check()

    username = name.split("_")
    firstname = username[0]
    lastname = "user" + username[1]
    #page.locator("#first_name").fill(firstname)
    page.fill("#first_name",firstname)
    # page.locator("#last_name").fill(lastname)
    page.fill("#last_name",lastname )
    # page.locator("#address1").fill("Sri Nilaya")
    page.fill("#address1","Sri Nilaya")
    #page.locator("#country").select_option("India")
    page.select_option("#country", "India")
    # page.locator("#state").fill("Telangana")
    page.fill("#state","Telangana")
    # page.locator("#city").fill("Hyderabad")
    page.fill("#city", "Hyderabad")
    # page.locator("#zipcode").fill("500058")
    page.fill("#zipcode", "500058")
    # page.locator("#mobile_number").fill("1234567890")
    page.fill("#mobile_number","1234567890" )
    page.get_by_role("button", name="Create Account").click()
    page.wait_for_load_state("networkidle")
    assert page.locator("text='Account Created!'").is_visible()
    page.get_by_role("link", name="Continue").click()

    assert page.locator(f"text=Logged in as {name}").is_visible()

    return page, name, email, password  # return to the test for use in deletion


import time
from playwright.sync_api import expect, Page


def register_user(page: Page, generate_unique_name, generate_unique_email):
    """
    Automates the user registration process on the Automation Exercise website.

    Args:
        page: The Playwright page object for interacting with the browser.
        generate_unique_name: A function to generate a unique user name.
        generate_unique_email: A function to generate a unique email address.

    Returns:
        A tuple containing the page object and the user's name, email, and password.
    """

    # Generate unique user credentials
    name = generate_unique_name()
    email = generate_unique_email()
    password = "Password@123"

    # Navigate to the website and verify the title
    page.goto("https://automationexercise.com/")
    page.wait_for_load_state("networkidle")
    expect(page).to_have_title("Automation Exercise")

    # Click the Signup / Login link
    page.get_by_role("link", name=" Signup / Login").click()
    expect(page.get_by_text("New User Signup!")).to_be_visible()

    # Fill in the signup form and submit
    page.get_by_placeholder("Name").fill(name)
    page.locator("[data-qa='signup-email']").fill(email)
    page.get_by_role("button", name="Signup").click()

    # Verify the page title and the 'Enter Account Information' heading
    expect(page).to_have_title("Automation Exercise - Signup")
    expect(page.locator("text='ENTER ACCOUNT INFORMATION'")).to_be_visible()

    # Fill in account details
    page.locator("#id_gender1").check()

    # Assert that name and email fields are pre-populated correctly
    expect(page.locator("#name")).to_have_value(name)
    expect(page.locator("#email")).to_have_value(email)

    page.get_by_label("Password *").fill(password)

    page.locator("#days").select_option("30")
    page.locator("#months").select_option("August")
    page.locator("#years").select_option("1990")

    # Check the newsletter and special offers checkboxes
    page.locator("#newsletter").check()
    page.locator("#optin").check()

    # Fill in personal details and address
    username = name.split("_")
    firstname = username[0]
    lastname = "user" + username[1]

    page.locator("#first_name").fill(firstname)
    page.locator("#last_name").fill(lastname)
    page.locator("#address1").fill("Sri Nilaya")
    page.locator("#country").select_option("India")
    page.locator("#state").fill("Telangana")
    page.locator("#city").fill("Hyderabad")
    page.locator("#zipcode").fill("500058")
    page.locator("#mobile_number").fill("1234567890")

    # Click the 'Create Account' button
    page.get_by_role("button", name="Create Account").click()
    page.wait_for_load_state("networkidle")

    # Verify the success message and continue
    expect(page.get_by_text("Account Created!")).to_be_visible()
    page.get_by_role("link", name="Continue").click()

    # Verify that the user is logged in
    expect(page.get_by_text(f"Logged in as {name}")).to_be_visible()

    return page, name, email, password