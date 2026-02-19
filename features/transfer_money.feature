Feature: Transfer money between accounts

  Scenario Outline: Successful transfer between accounts
    Given I am logged in as "<user>"
    When I transfer "<amount>" from "<from_account>" to "<to_account>"
    Then I should see a success message

    Examples:
      | user      | from_account | to_account | amount |
      | dev_user  | Savings      | Checking   | 100    |
      | dev_user  | Checking     | Savings    | 50     |
