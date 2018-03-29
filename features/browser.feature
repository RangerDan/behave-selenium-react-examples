Feature: showing off behave with selenium integration

@fixture.browser.firefox @wip
Scenario: Search test scenario on Firefox
  Given I navigate to "http://www.google.com"
  When I search for "Hoopy Froods"
  Then the page contains "Hitchhiker"

@fixture.browser.chrome @wip
Scenario: Search test scenario on Chrome
  Given I navigate to "http://www.google.com"
  When I search for "Hoopy Froods"
  Then the page contains "Hitchhiker"
