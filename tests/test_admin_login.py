import os

from pages.login_page import LoginPage
from utils.helpers import read_json


def test_login(base_url, driver):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'login_data.json')
    login_data = read_json(file_path)['login']

    driver.get(base_url)

    login_page  = LoginPage(driver)
    login_page.enter_username(login_data["username"])
    login_page.enter_password(login_data["password"])
    login_page.click_login()

    # Wait for the URL to change (this is a simple example, consider using WebDriverWait for a more robust solution)
    driver.implicitly_wait(10)
# ====================================================Assertions======================================================================
    # Get the current URL
    current_url = driver.current_url

    # Assert that the current URL matches the expected URL
    assert current_url == login_data["expected_url"], f"Expected URL '{login_data['expected_url']}', but got '{current_url}'"