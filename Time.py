# from datetime import datetime, time
#
# # Get current time
# now = datetime.now().time()
#
# # Define time range
# start = time(0, 0)    # 12:00 AM
# end = time(12, 0)     # 12:00 PM
#
# # Check if current time is within the range
# if start <= now < end:
#     print("Good Morning")
# else:
#     print("Time is NOT between 12AM and 12PM")
from asyncio import wait_for


def test_register_user(page, generate_unique_name, generate_unique_email):
    name = generate_unique_name
    email = generate_unique_email
    password = "Password@123"
    print(name, email, password)

    page.goto("https://automationexercise.com/")
