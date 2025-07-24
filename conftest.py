import random
import time

import pytest
from playwright.sync_api import sync_playwright

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
    name = generate_unique_name
    email = generate_unique_email
    password = "Password@123"

    page.goto("https://automationexercise.com/")
    page.wait_for_load_state("networkidle")

    assert page.title() == "Automation Exercise"
    page.get_by_role("link", name=" Signup / Login").click()
    assert page.get_by_text("New User Signup!").is_visible()

    page.get_by_placeholder("Name").fill(name)
    page.locator("//input[@data-qa='signup-email']").fill(email)
    page.get_by_role("button", name="Signup").click()
    time.sleep(2)

    assert page.title().__contains__("Automation Exercise")
    assert page.locator("text='Enter Account Information'").is_visible()

    page.locator("#id_gender1").check()
    assert page.locator("#name").input_value() == name
    assert page.locator("#email").input_value() == email
    page.get_by_label("Password *").fill(password)

    page.locator("#days").select_option("30")
    page.locator("#months").select_option("August")
    page.locator("#years").select_option("1990")

    page.locator("#newsletter").check()
    page.locator("//input[@name='optin']").check()

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

    page.get_by_role("button", name="Create Account").click()
    page.wait_for_load_state("networkidle")
    assert page.locator("text='Account Created!'").is_visible()
    page.get_by_role("link", name="Continue").click()

    assert page.locator(f"text=Logged in as {name}").is_visible()

    return page, name, email, password  # return to the test for use in deletion


