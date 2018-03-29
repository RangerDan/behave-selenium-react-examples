# -- FILE: /fixtures.py
from behave import fixture, use_fixture
from selenium.webdriver import Firefox, Chrome
import time

# -- FIXTURE: Use generator-function
@fixture
def browser_firefox(context, timeout = 30, **kwargs):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    context.browser = Firefox()
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.close()

@fixture
def browser_chrome(context, timeout = 30, **kwargs):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    context.browser = Chrome()
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.close()

# Wait up to wait # of seconds for something to happen
def wait_for_result_in_source(context, result, wait=10):
    now = time.time()
    while (time.time() - now < wait):
        if result is not None and result in context.browser.page_source:
            return True
    return False
