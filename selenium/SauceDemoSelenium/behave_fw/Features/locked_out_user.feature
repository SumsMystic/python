Feature: As a locked_out user, I want to verify if correct error message is shown upon login attempt


@total
Scenario: Test for locked out user
    When I login as locked out user
    Then I should see the appropriate error message