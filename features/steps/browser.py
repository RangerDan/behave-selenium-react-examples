from behave import *
from selenium.webdriver.common.keys import Keys
from fixtures import wait_for_result_in_source


# Givens
@given(u'I navigate to "{testUrl}"')
def step_impl(context,testUrl):
    context.browser.get(testUrl)
    assert 'Google' in context.browser.title


# Whens
@when(u'I search for "{query}"')
def step_impl(context,query):
    elem = context.browser.find_element_by_name("q")
    elem.send_keys(query)
    elem.send_keys(Keys.RETURN)
    assert query in context.browser.page_source


# Thens
@then(u'the page contains "{result}"')
def step_impl(context,result):
    assert wait_for_result_in_source(context, result, 10) is True


# Combined Steps
@given(u'I search on "{testUrl}" for "{query}"')
def step_impl(context, query, testUrl):
    context.execute_steps(u'''
        Given I navigate to "{testUrl}"
        When I search for "{query}"
        Then the page contains "Hitchhiker"
    '''.format(testUrl=testUrl, query=query))
