# selenium_101_certification
## Welcome to ![LambdaTest Logo](https://github.com/hodehoujolive/selenium_101_certification/blob/master/S101-NH5B2N.jpeg) - Python-UnitTest-Selenium Sample
--- 

### Step 1 : Environment Setup

#### Lambdatest Credentials

Set LambdaTest username and access key in environment variables in the file `lamdatest.env`

Replace the values with your credentials, you can find them at (https://www.lambdatest.com/capabilities-generator/)

```
ln 1: export LT_USERNAME="Your Username"
ln 2: export LT_ACCESS_KEY="Your Access key"
```
![Lamdatest Credentials](/assets/screenshot.png)

After your save your credentials at `lambdatest.env` please run the command: 

```
$ source lambdatest.env
```

### Step 2: Setting up your test capabilites

You can genegate the test capabilites at (https://www.lambdatest.com/capabilities-generator/) and choose **Python** as the language. 

Now, can setup the capabilites of the test in the `single_test.py` file at: 

```
ln 13: desired_caps = {
ln 14:           "build": 'PyunitTest sample build',
ln 15:            "name": 'Py-unittest',
ln 16:           "platform": 'OS X El Capitan',
ln 17:            "browserName": 'chrome',
ln 18:           "version": '81.0',
ln 19:           "console": 'true',
ln 20:           "network":'true'
ln 21:        }

```

You can setup the capabilites of your test in the `parallel_test.py` file at: 

```
browsers = [
    {"build": 'PyunitTest sample build',"name": "Test 1", "platform": "Windows 10","browserName": "Chrome", "version": "86.0"},
    {"build": 'PyunitTest sample build',"name": "Test 2", "platform": "Windows 10","browserName": "Firefox", "version": "82.0"}
]
```

### Step 3: Running Tests
To start a single test Run following command: <br/><br/>

```
$ pipenv run python -m pytest
```

To start a parallel test Run the following command: <br/><br/>
```
$ python tests/parallel_test.py
```

## About LambdaTest

[LambdaTest](https://www.lambdatest.com/) is a cloud based selenium grid infrastructure that can help you run automated cross browser compatibility tests on 2000+ different browser and operating system environments. LambdaTest supports all programming languages and frameworks that are supported with Selenium, and have easy integrations with all popular CI/CD platforms. It's a perfect solution to bring your [selenium automation testing](https://www.lambdatest.com/selenium-automation) to cloud based infrastructure that not only helps you increase your test coverage over multiple desktop and mobile browsers, but also allows you to cut down your test execution time by running tests on parallel.

### For further References

##### [SeleniumHQ Documentation](http://www.seleniumhq.org/docs/)
##### [UnitTest Documentation](https://docs.python.org/2/library/unittest.html)
