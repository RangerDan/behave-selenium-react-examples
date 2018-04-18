@selenium
Feature: showing off behave with selenium integration
  #http://selenium-python.readthedocs.io/

@fixture.browser.firefox @wip
Scenario: Search test scenario on Firefox
  Given I navigate to "http://www.google.com"
  When I search for "Hoopy Froods"
  Then the page contains "Hitchhiker"

@fixture.browser.chrome
Scenario: Search test scenario on Chrome
  Given I navigate to "http://www.google.com"
  When I search for "Hoopy Froods"
  Then the page contains "Hitchhiker"

@fixture.browser.chrome
Scenario: Search again by clearing the input field
  Given I search on "https://www.google.com" for "Hoopy Froods"

Scenario: Screenshots?
Scenario: Multiple browsers?
Scenario: Remote Selenium
