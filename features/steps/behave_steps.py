# -- FILE: steps/behave_steps.py
# CONTAINS: Behave step definitions
from behave import *


@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement a test')
def step_impl(context):
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False


@given(u'I set a step value')
def step_impl(context):
    assert context.notSet is True
    context.notSet = False
    # Expecting this to change in before_step


@given(u'I set a scenario value')
def step_impl(context):
    assert context.scenarioSet is True
    context.scenarioSet = False
    # Expecting this will not change


@given(u'I set a feature value')
def step_impl(context):
    assert context.featureSet is True
    context.featureSet = False
    # Expecting this will not change


@then(u'the step value will have changed between steps')
def step_impl(context):
    # Will fail if before_step does not change it
    assert context.notSet is True


@then(u'the scenario value will not change between steps')
def step_impl(context):
    # Will fail if before_step does not change it
    assert context.scenarioSet is False


@then(u'the feature value will not change between steps')
def step_impl(context):
    # Will fail if before_step does not change it
    assert context.featureSet is False


@given(u'we have the following animals')
def step_impl(context):
    # testing some asserts
    for row in context.table:
        assert row['animals'] in ['lions','tigers','bears']


@when(u'I sing')
def step_impl(context):
    # testing some asserts
    assert 'Old McDonald' in context.text


@then(u'the group sings {test}')
def step_impl(context,test):
    # testing some asserts
    assert 'E' in test


@step(u'this test can be called from Given, When or Then')
def step_impl(context):
    assert True


@when(u'I do previously implemented steps')
def step_impl(context):
    context.execute_steps(u'''
        Given we have behave installed
        When we implement a test
        Then behave will test it for us!
    ''')


@when(u'I pass and store text "{text}"')
def step_impl(context, text):
    context.store = text


@then(u'the stored text matches "{text}"')
def step_impl(context,text):
    assert context.store == text


@when(u'I pass and store digits {digits:d}')
def step_impl(context, digits):
    context.store = digits


@then(u'the stored digits are greater than {gt:d}')
def step_impl(context,gt):
    assert context.store > gt
