from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, 'email')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'submit')

    def enter_username(self, username):
        username_field = self.driver.find_element(*self.email_input)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(*self.password_input)
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
