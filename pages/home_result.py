from selenium.webdriver.common.by import By

class LambdaHomeResult:

    # Locators
    span_slider = (By.XPATH, '/html/body/div[2]/section[3]/div/div[2]/div[2]/div/div[1]/span')
    submit_success = (By.XPATH, '/html/body/div[2]/div/h1')


    # Initializer
    def __init__(self, browser):
        self.browser = browser

    
    # Interaction Methods
    def span_slider_value(self):
        span_slider = self.browser.find_element(*self.span_slider)
        value = span_slider.get_attribute('style')
        return value
    
    def alert_value(self):
        obj = self.browser.switch_to.alert
        value = obj.text
        print(value)
        return value

    def submit_success_value(self):
        submit_success = self.browser.find_element(*self.submit_success)
        value = submit_success.text
        return value
        
    

    def title(self):        
        return self.browser.title