from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import urllib

class LambdaHomePage:


    #locators
    EMAIL_INPUT = (By.ID, 'developer-name')
    POPULATE_INPUT = (By.ID, 'populate')

    FREQUENCY = (By.ID, 'month')   
    FACTORS =(By.ID, 'customer-service')
    PAYMENTS =(By.ID, 'preferred-payment')
    PURCHASE =(By.ID, 'tried-ecom')
    RATE =(By.CSS_SELECTOR, '#slider')
    FEEDBACK =(By.TAG_NAME, 'textarea')
    UPLOAD =(By.ID, 'file')
    SUBMIT=(By.ID, 'submit-button')
    JENKINS_IMG = (By.XPATH, '/html/body/div[2]/section[6]/div/div[2]/ul/li[1]/a/img')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction methods

    def enter_email(self, email):
        email_input = self.browser.find_element(*self.EMAIL_INPUT)
        email_input.send_keys(email)

        populate_input = self.browser.find_element(*self.POPULATE_INPUT)
        populate_input.click()
    
    def accept_popup(self):
        obj = self.browser.switch_to.alert
        obj.accept()

    def answer_question(self):
        frequency = self.browser.find_element(*self.FREQUENCY)
        frequency.click()

        factors = self.browser.find_element(*self.FACTORS)
        factors.click()

        payments = Select(self.browser.find_element(*self.PAYMENTS))
        select_payments = payments.select_by_index(1)

        purchase = self.browser.find_element(*self.PURCHASE)
        purchase.click()

        rate = self.browser.find_element(*self.RATE)
        move_rate = ActionChains(self.browser)

        self.browser.execute_script("return arguments[0].scrollIntoView(true);", purchase)
        move_rate.click_and_hold(rate).move_by_offset(190, 100).release().perform()

        feedback = self.browser.find_element(*self.FEEDBACK)
        feedback.clear()
        feedback.send_keys("i love selenium with python")


    def open_new_tab(self, tab_url):
        self.browser.execute_script("window.open('');")
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.get(tab_url)

    def download_jenkins_image(self):
        with open('jenkins.svg', 'wb') as file:
            img = self.browser.find_element(*self.JENKINS_IMG)
            file.write(img.screenshot_as_png)

    def switch_back(self):
        self.browser.switch_to.window(self.browser.window_handles[0])
        
    def upload_file(self):
        upload = self.browser.find_element(*self.UPLOAD)
        upload.send_keys("/home/jolivehodehou/Desktop/lambda_test/jenkins.svg")

    def submit_form(self):
        submit = self.browser.find_element(*self.SUBMIT)
        submit.click()






