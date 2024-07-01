import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json

from pages.customer_list_page import CustomerListPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.user_creation_page import UserCreationPage
from utils.helpers import read_json

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    """Fixture to provide the base URL for the application."""
    return "https://testautomationchallenge-manager.testenv.impel.io"

@pytest.fixture(scope="session")
def read_json_fix():
    """Fixture to read JSON data files."""
    def _read_json(relative_path):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, relative_path)
        with open(file_path, 'r') as file:
            return json.load(file)
    return _read_json

@pytest.fixture(scope="module")
def login(driver):
    login_data = read_json('data/login_data.json')["login"]
    driver.get("https://testautomationchallenge-manager.testenv.impel.io")
    login_page = LoginPage(driver)
    login_page.enter_username(login_data["username"])
    login_page.enter_password(login_data["password"])
    login_page.click_login()
    yield

@pytest.fixture(scope="module")
def dashboard(driver, login):
    dashboard_page = DashboardPage(driver)
    dashboard_page.navigate_to_customer_list()

@pytest.fixture(scope="module")
def customer_list_page(driver, login, dashboard):
    customerList = CustomerListPage(driver)
    customerList.clickonBtnAddCustomer()
    yield customerList

@pytest.fixture(scope="module")
def user_creation(driver, login, dashboard, customer_list_page):
    user_creationPage = UserCreationPage(driver)
    yield user_creationPage

@pytest.fixture(scope="module")
def user_data(read_json_fix):
    """Fixture to provide user creation data."""
    return read_json('data/user_creation_data.json')["user_data"]



# ==========================================================================================================================================


