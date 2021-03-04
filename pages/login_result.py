from selenium.webdriver.common.by import By

class LambdaLoginResult:

    # Locators
    heading = (By.XPATH, '/html/body/div[2]/section[1]/h1')


    # Initializer
    def __init__(self, browser):
        self.browser = browser

    
    # Interaction Methods
    def heading_value(self):
        heading = self.browser.find_element(*self.heading)
        value = heading.get_attribute('class')
        return value
    

    def title(self):        
        return self.browser.title