Feature: showing off behave with selenium integration

@fixture.browser.firefox @wip
Scenario: Yahoo test scenario
  Given I navigate to "http://www.google.com"
  When I search for "Hoopy Froods"
  Then the page contains "Hitchhiker"
