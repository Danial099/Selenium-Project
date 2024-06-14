import pytest
from selenium.webdriver.common.by import By
from pages.dashboard_page import DashboardPage

@pytest.mark.usefixtures('login')
@pytest.mark.parametrize("expected_url, customer_list_heading_selector", [
    ("https://testautomationchallenge-manager.testenv.impel.io/my-customer/?_acid=3964", "div[class='row'] h3"),
    # Add more scenarios if needed
])
def test_dashboard(driver, expected_url, customer_list_heading_selector):

    dashboard_Page = DashboardPage(driver)
    dashboard_Page.navigate_to_customer_list()

# ===================================================Assertions==================================================
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL '{expected_url}', but got '{current_url}'"
    # additional assertion
    customer_list_heading = driver.find_element(By.CSS_SELECTOR, customer_list_heading_selector)
    assert customer_list_heading is not None, "Customer List heading not found on the page"
