import pytest
from selenium.webdriver.common.by import By

from pages.customer_list_page import CustomerListPage


@pytest.mark.usefixtures('dashboard')
@pytest.mark.parametrize("expected_url, customer_list_heading_selector", [
    ("https://testautomationchallenge-manager.testenv.impel.io/my-customer/create?_acid=3964", "div[class='row'] h3"),
    # Add more scenarios if needed
])

def test_customer_list(driver, dashboard, expected_url, customer_list_heading_selector):
    customerList = CustomerListPage(driver)
    customerList.clickonBtnAddCustomer()
    driver.implicitly_wait(10)

# ===================================================Assertions==================================================
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL '{expected_url}', but got '{current_url}'"
    # additional assertion
    customer_list_heading = driver.find_element(By.CSS_SELECTOR, customer_list_heading_selector)
    assert customer_list_heading is not None, "Customer List heading not found on the page"
    driver.implicitly_wait(10)
