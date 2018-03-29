# -- FILE: features/environment.py
# CONTAINS: Browser fixture setup and teardown
from behave import fixture, use_fixture
from fixtures import browser_firefox, browser_chrome

BEHAVE_DEBUG_ON_ERROR = False

def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")

def before_all(context):
    setup_debug_on_error(context.config.userdata)

def before_feature(context,feature):
    context.featureSet = True

def before_scenario(context,scenario):
    context.scenarioSet = True

def before_tag(context,tag):
    if tag == 'fixture.browser.firefox':
        use_fixture(browser_firefox, context, timeout=10)
    if tag == 'fixture.browser.chrome':
        use_fixture(browser_chrome, context, timeout=10)

def before_step(context, step):
    context.notSet = True

def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        # -- ENTER DEBUGGER: Zoom in on failure location.
        # NOTE: Use IPython debugger, same for pdb (basic python debugger).
        import ipdb
        ipdb.post_mortem(step.exc_traceback)
