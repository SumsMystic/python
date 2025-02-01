Feature
As a standard user  I want to add and remove items from my cart, view the bill and checkout

Scenario: Add and remove items from cart
    Given I login as standard user
    When I add the following items to the cart
        | item_name                 |
        | Sauce Labs Backpack       |
        | Sauce Labs Fleece Jacket  |
    And I remove the following items from the cart
        | item_name                 |
        | Sauce Labs Fleece Jacket  |
    And I add the following items to the cart
        | item_name                 |
        | Sauce Labs OneSie         |
    Then the cart should contain the following items
        | item_name                 |
        | Sauce Labs Backpack       |
        | Sauce Labs OneSie         |
    And the cart should show the bill of the items
    And I should be able to checkout using following details
        | first_name | last_name | postal_code |
        | John       | Doe       | 12345       |
    And the cart should be empty after checkout
