import json
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


def login_with_new_user(driver, base_url):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'new_login_data.json')
    with open(file_path, 'r') as file:
        new_login_data = json.load(file)
    driver.get(base_url)
    # create new login page object
    new_login_page = LoginPage(driver)
    new_login_page.enter_username(new_login_data["email"])
    new_login_page.enter_password(new_login_data["password"])
    new_login_page.click_login()
    driver.implicitly_wait(10)
    WebDriverWait(driver, 10).until(EC.url_to_be(new_login_data["expected_url"]))

    assert driver.current_url == new_login_data[
        "expected_url"], f"Expected URL '{new_login_data['expected_url']}', but got '{driver.current_url}'"

    user_name_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "ul[class='nav navbar-nav navbar-right'] li[class='dropdown']"))
    )
    assert user_name_element is not None, "User name element not found. Login might have failed."
    user_name_text = user_name_element.text
    expected_user_name = new_login_data["email"].split('@')[0]  # Assuming the username is the email prefix
    assert user_name_text == expected_user_name, f"Expected user name '{expected_user_name}', but got '{user_name_text}'"
    print(f"Login successful. User name: {user_name_text}")
    print(user_name_text)
    driver.implicitly_wait(10)


def test_login_with_new_user(driver, base_url):
    # Use the function to log in with new user credentials
    login_with_new_user(driver, base_url)
