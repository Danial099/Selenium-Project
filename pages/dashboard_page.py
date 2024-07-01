
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.customers_menu = (By.LINK_TEXT, 'Customers')
        self.list_submenu = (By.LINK_TEXT, 'List')
        self.wait = WebDriverWait(driver, 1000)

    def navigate_to_customer_list(self):
        self.driver.find_element(*self.customers_menu).click()
        self.driver.find_element(*self.list_submenu).click()

