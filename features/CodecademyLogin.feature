@selenium
Feature: Account management on codecademy using saved credentials
  Users want to be able to log in from the homepage
    So they can get to their courses and resources

@fixture.browser.firefox @fixture.ca.credentials
Scenario: Log in from home page
  Given I navigate to "https://www.codecademy.com/login"
  When I select the input field named "user[login]"
  And I key into the current element stored value "username"
  And I select the element by id "login__user_password"
  And I key into the current element stored value "password"
  And I submit the current form
  Then the page contains the stored "username"
  And I take a screenshot and name it "loggedIn"

@fixture.browser.firefox @fixture.ca.credentials
Scenario: Check for alerts
  Given I log in on codecademy
  When I select the element by css "div[class^='bell']"
  And I click the current element
  And I take a screenshot and name it "notifications"
  Then the notifications popup displays

@fixture.browser.firefox @fixture.ca.credentials
Scenario: View Profile
  Given I log in on codecademy
  When I click my profile picture
  Then the account popover displays
  And a link to My Account is in the popup
  And a link to Help is in the popup
  And a link to Logout is in the popup
  And I take a screenshot and name it "myaccountpopup"

@fixture.browser.firefox @fixture.ca.credentials
Scenario: Logged in user can logout
  Given I log in on codecademy
  And I click my profile picture
  And the account popover displays
  When I click the link to Logout in the popup
  Then the current URL contains "codecademy.com"
  And I take a screenshot and name it "loggedOut"
  # TODO Test kind of weak. Attempt to use a resource only for logged in users?

@fixture.browser.firefox @fixture.ca.credentials
Scenario: A logged in user can see their profile information
  Given I log in on codecademy
  And I click my profile picture
  And the account popover displays
  When I click the link to My Account in the popup
  Then the current URL contains "codecademy.com/account"
  Then the username field contains the stored "username"
  And I take a screenshot and name it "myAccount"

@fixture.browser.firefox @fixture.ca.credentials
Scenario: A logged in user can change their password
  Given I log in on codecademy
  Given I go to My Account
  And I click the Change Password tab
  And I store key "new_password" with value "NewReactPass123"
  # Make a change
  When I change my password from stored "password" to stored "new_password"
  And I log in on the current page with stored "new_password"
  And I take a screenshot and name it "new_password_login"
  # Undo the change
  Given I go to My Account
  When I click the Change Password tab
  Then I change my password from stored "new_password" to stored "password"
