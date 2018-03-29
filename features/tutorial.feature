Feature: showing off behave

  Scenario: Run a simple test
    Given we have behave installed
    When we implement a test
    Then behave will test it for us!

  Scenario Outline: Table, Multi-line Example
    Given we have the following animals:
      | animals |
      | lions   |
      | tigers  |
      | bears   |
    When I sing
      """
      Old McDonald had a farm...
      """
    Then the group sings <line>

    Examples:
      | line      |
      | E-I-E-I-O |

  Scenario: Test before and after features, scenarios, steps
    Given I set a step value
    And I set a scenario value
    And I set a feature value
    Then the step value will have changed between steps
    And the scenario value will not change between steps
    And the feature value will not change between steps

  Scenario: Tests the step implementation @step
    Given this test can be called from Given, When or Then
    When this test can be called from Given, When or Then
    Then this test can be called from Given, When or Then

  Scenario: Test steps can be combined inside an implementation
    When I do previously implemented steps

  Scenario: Testing parse parameters for free text
    When I pass and store text "test text with a space"
    Then the stored text matches "test text with a space"

    Scenario: Testing parse parameters for digits without quotes
      When I pass and store digits 123456
      Then the stored digits are greater than 100000
