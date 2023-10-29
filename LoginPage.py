from selenium.webdriver.common.by import By

USERNAME_ID = "username"
PASSWORD_ID = "password"
LOGIN_ID = "log-in"


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = self.driver.find_element(By.ID, USERNAME_ID)
        self.password_field = self.driver.find_element(By.ID, PASSWORD_ID)
        self.login_button = self.driver.find_element(By.ID, LOGIN_ID)

    def login(self, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.login_button.click()
