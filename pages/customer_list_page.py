from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class CustomerListPage:
    def __init__(self, driver):
        self.driver = driver
        self.btn_add_customer = (By.CLASS_NAME, 'btn-primary')
        self.search_box = (By.ID, '#search')
        self.user_nav_bar = (By.CSS_SELECTOR, "a[id = 'navbar-login-menu']")
        self.user_logout = (By.CSS_SELECTOR, "a[href='/logout?_acid=3964']")

    def clickonBtnAddCustomer(self):
        self.driver.find_element(*self.btn_add_customer).click()

    def search_by_name(self, name):
        name_field = self.driver.find_element(*self.search_box)
        name_field.clear()
        name_field.send_keys(name)


    def Click_user_navBar(self):
        self.driver.find_element(*self.user_nav_bar).click()

    def Click_user_Logout(self):
        self.driver.find_element(*self.user_logout).click()

