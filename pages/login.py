from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LambdaLoginPage:

    #url
    url = 'https://www.lambdatest.com/automation-demos/'

    #locators
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, '/html/body/div[2]/section[2]/div/div/form/div/button')
    COOKIE = (By.XPATH, '/html/body/div[1]/header/div[1]/div/div/div[2]/a[1]')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction methods

    def load(self):
        self.browser.get(self.url)
        self.browser.implicitly_wait(30)

    def login(self, username, password):
        username_input = self.browser.find_element(*self.USERNAME_INPUT)
        username_input.send_keys(username)

        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

        cookie = self.browser.find_element(*self.COOKIE)
        cookie.click()

        login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        
        login_button.click()
