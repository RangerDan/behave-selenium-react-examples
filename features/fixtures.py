# -- FILE: /fixtures.py
from behave import fixture
from selenium.webdriver import Firefox, Chrome, DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# -- FIXTURE: Use generator-function
@fixture
def browser_firefox(context, timeout=30):
    capabilities = DesiredCapabilities.FIREFOX
    capabilities["moz:firefoxOptions"] = {
        "log": {
            "level": "trace",
        },
    }
    context.browser = Firefox(timeout=timeout, capabilities=capabilities)
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.close()


@fixture
def browser_chrome(context):
    context.browser = Chrome()
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.close()


@fixture
def ca_credentials(context):
    context.store['username'] = 'ReactTestUser'
    context.store['password'] = 'ReactTestUser123'


# Wait up to wait # of seconds for something to happen
def wait_for_result_in_source(context, result, wait=10):
    wait = WebDriverWait(context.browser, timeout=wait)
    if wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), result)):
        return True
    return False
