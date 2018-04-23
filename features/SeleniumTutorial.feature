@selenium
Feature: showing off behave with selenium integration
  #http://selenium-python.readthedocs.io/

@fixture.browser.chrome
Scenario: Search test scenario on Chrome
  Given I navigate to "https://www.google.com"
  When I search for "Hoopy Froods"
  Then the page contains "Hitchhiker"
  And I take a screenshot and name it "chrome-search"

@fixture.browser.firefox
Scenario: Search test scenario on Firefox
  Given I navigate to "http://www.google.com"
  When I search for "Hoopy Froods"
  Then the page contains "Hitchhiker"
  And I take a screenshot and name it "firefox-search"

# TODO: Flesh out these scenarios
Scenario: Multiple browsers?
Scenario: Remote Selenium
