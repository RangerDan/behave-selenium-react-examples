# -- FILE: steps/browser_steps.py
# CONTAINS: Browser step definitions
# TODO: Implement page objects to simplify locating objects
# TODO: Make a context.wait to remove the repetition in each step
# TODO: Stop using @given, @when, @then; only use @step?
from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from fixtures import wait_for_result_in_source


# Givens
@given(u'I click the login tab')
def step_impl(context):
    # TODO Maybe find a better locator strategy that the reactid?
    elem = context.browser.find_element_by_css_selector('div[data-reactid="4"]')
    elem.click()
    context.current_element = elem


# Whens
@when(u'I search for "{query}"')
def step_impl(context, query):
    elem = context.browser.find_element_by_name("q")
    elem.send_keys(query)
    elem.send_keys(Keys.RETURN)
    assert query in context.browser.page_source


@when(u'I click my profile picture')
def step_impl(context):
    elem = context.browser.find_element_by_id("dropdown-toggle")
    elem.click()


@when(u'I click the link to My Account in the popup')
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=10)
    elem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class*="popover"] a[id="edit-account-link"]')))
    elem.click()


@when(u'I click the link to the Community Forums in the popup')
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=10)
    elem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class*="popover"] a[id="forums-link"]')))
    elem.click()


@when(u'I click the link to Help in the popup')
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=10)
    elem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class*="popover"] a[id="help-link"]')))
    elem.click()


@when(u'I click the link to Logout in the popup')
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=10)
    elem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class*="popover"] a[id="sign-out-link"]')))
    elem.click()


# Thens
@then(u'the page contains "{result}"')
def step_impl(context, result):
    assert wait_for_result_in_source(context, result, 10) is True


@then(u'the page contains the stored "{stored_value}"')
def step_impl(context, stored_value):
    assert wait_for_result_in_source(context, context.store[stored_value], 10) is True


@then(u'the notifications popup displays')
def step_impl(context):
    assert wait_for_result_in_source(context, 'You have no new notifications.', 10) is True


@then(u'a link to My Account is in the popup')
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=10)
    assert wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class*="popover"] a[id="edit-account-link"]')))


@then(u'a link to the Community Forums is in the popup')
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=10)
    assert wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class*="popover"] a[id="forums-link"]')))


@then(u'a link to Help is in the popup')
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=10)
    assert wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class*="popover"] a[id="help-link"]')))


@then(u'a link to Logout is in the popup')
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=10)
    assert wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class*="popover"] a[id="sign-out-link"]')))


# Generic Steps
@step(u'I select the input field named "{selector_name}"')
def step_impl(context, selector_name):
    wait = WebDriverWait(context.browser, timeout=10)
    elem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="%s"]' % selector_name)))
    context.current_element = elem


@step(u'I select the element by id "{element_id}"')
def step_impl(context, element_id):
    wait = WebDriverWait(context.browser, timeout=10)
    elem = wait.until(EC.visibility_of_element_located((By.ID, element_id)))
    context.current_element = elem


@step(u'I select the element by css "{selector}"')
def step_impl(context, selector):
    wait = WebDriverWait(context.browser, timeout=10)
    elem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    # elem = context.browser.find_element_by_css_selector(selector)
    context.current_element = elem


@step(u'I store key "{new_key}" with value "{new_value}"')
def step_impl(context, new_key, new_value):
    context.store[new_key] = new_value


@step(u'I key the stored "{stored_value}" into the "{element}" field')
def step_impl(context, stored_value, element):
    toKey = context.store[stored_value]
    elem = context.browser.find_element_by_css_selector(element)
    elem.send_keys(toKey)
    context.current_element = elem


@step(u'I key into the current element "{text}"')
def step_impl(context, text):
    context.current_element.send_keys(text)


@step(u'I key into the current element stored value "{stored_value}"')
def step_impl(context, stored_value):
    context.current_element.send_keys(context.store[stored_value])


@step(u'I submit the current form')
def step_impl(context):
    context.current_element.submit()


@step(u'I click the current element')
def step_impl(context):
    context.current_element.click()


@step(u'I take a screenshot and name it "{screenshot_name}"')
def step_impl(context, screenshot_name):
    context.browser.save_screenshot('./screenshots/%s.png' % screenshot_name)


@step(u'I navigate to "{test_url}"')
def step_impl(context, test_url):
    context.browser.get(test_url)


@step(u'the current URL contains "{expected_url}"')
def step_impl(context, expected_url):
    assert expected_url in context.browser.current_url


@step(u'the username field contains the stored "{stored_value}"')
def step_impl(context, stored_value):
    wait = WebDriverWait(context.browser, timeout=10)
    elem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="user_username"]')))
    assert elem.get_attribute("value") == context.store[stored_value]


@step(u'I click my profile picture')
def step_impl(context):
    elem = context.browser.find_element_by_id("dropdown-toggle")
    elem.click()


@step(u'the account popover displays')
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=10)
    assert wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class*="popover"]')))


@step(u'I click the Change Password tab')
def step_impl(context):
    elem = context.browser.find_element_by_css_selector('a[href="/account/password"]')
    elem.click()


@step(u'I change my password from stored "{old_pass}" to stored "{new_pass}"')
def step_impl(context, old_pass, new_pass):
    wait = WebDriverWait(context.browser, timeout=10)
    elem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="password"]')))
    elem.send_keys(context.store[new_pass])
    elem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="password_confirmation"]')))
    elem.send_keys(context.store[new_pass])
    elem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="current_password"]')))
    elem.send_keys(context.store[old_pass])
    elem.submit()


# Combined Steps
@given(u'I search on "{test_url}" for "{query}"')
def step_impl(context, query, test_url):
    context.execute_steps(u'''
        Given I navigate to "{test_url}"
        When I search for "{query}"
        Then the page contains "Hitchhiker"
    '''.format(test_url=test_url, query=query))


@given(u'I log in on codecademy')
def step_impl(context):
    context.execute_steps(u'''
        Given I navigate to "https://www.codecademy.com/login"
        When I select the input field named "user[login]"
        And I key into the current element stored value "username"
        And I select the element by id "login__user_password"
        And I key into the current element stored value "password"
        And I submit the current form
        Then the page contains the stored "username"
    ''')


@given(u'I go to My Account')
def step_impl(context):
    context.execute_steps(u'''
        Given I click my profile picture
        And the account popover displays
        When I click the link to My Account in the popup
        Then the current URL contains "codecademy.com/account"
        And the username field contains the stored "username"
    ''')


@step(u'I log in on the current page with stored "{stored_password}"')
def step_impl(context, stored_password):
    context.execute_steps(u'''
        When I select the input field named "user[login]"
        And I key into the current element stored value "username"
        And I select the element by id "login__user_password"
        And I key into the current element stored value "%s"
        And I submit the current form
        Then the page contains the stored "username"
    ''' % stored_password)
