import pytest
import time

from pages.login_result import LambdaLoginResult
from pages.login import LambdaLoginPage
from pages.home import LambdaHomePage
from pages.home_result import LambdaHomeResult

username = "lambda"
password = "lambda123"
email = "jolivehodehou7@gmail.com"
feedback= "feedback text"
tab_url = 'https://www.lambdatest.com/selenium-automation'



def test_lambda(browser):

    login_page = LambdaLoginPage(browser)
    login_result_page = LambdaLoginResult(browser)

    home_page = LambdaHomePage(browser)
    home_result_page = LambdaHomeResult(browser)

    login_page.load()
    login_page.login(username, password)

    time.sleep(3)

    assert "Selenium Playground" in login_result_page.title()
    assert "Selenium-heading" in login_result_page.heading_value()

    time.sleep(3)
    home_page.enter_email(email)

    time.sleep(2)
    home_page.accept_popup()

    time.sleep(2)

    home_page.answer_question()
    assert "left: 88.8889%;" in home_result_page.span_slider_value()

    time.sleep(5)

    home_page.open_new_tab(tab_url)
    time.sleep(5)

    home_page.download_jenkins_image()
    time.sleep(5)
    
    home_page.switch_back()
    time.sleep(2)

    home_page.upload_file()

    assert "your image upload sucessfully!!" in home_result_page.alert_value()
    print("upload test as passed")
    time.sleep(2)
    home_page.accept_popup()

    time.sleep(2)

    home_page.submit_form()
    time.sleep(5)

    assert "Thank you!" in home_result_page.submit_success_value()
    print("submit test as passed")



    
