Feature: As a standard user, I want to add and remove items from my cart, view the bill, and checkout

@total
Scenario: End To End test for standard user
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
        | Sauce Labs Onesie         |
    Then the cart should contain the following items
        | item_name                 |
        | Sauce Labs Backpack       |
        | Sauce Labs Onesie         |
    And the cart should show the bill of the items
    And I should be able to checkout using following details
        | first_name | last_name | postal_code |
        | John       | Doe       | 12345       |
    And the cart should be empty after checkout

@total
Scenario: Add items to cart and view the bill and checkout
    Given I login as standard user
    When I add the following items to the cart
        | item_name                 |
        | Sauce Labs Backpack       |
        | Sauce Labs Fleece Jacket  |
    Then the cart should contain the following items
        | item_name                 |
        | Sauce Labs Backpack       |
        | Sauce Labs Fleece Jacket  |
    And the cart should show the bill of the items
    And I should be able to checkout using following details
        | first_name | last_name | postal_code |
        | John       | Doe       | 12345       |
    And the cart should be empty after checkout

@smoke
Scenario: Add items to cart
    Given I login as standard user
    When I add the following items to the cart
        | item_name                 |
        | Sauce Labs Backpack       |
    Then the cart should contain the following items
        | item_name                 |
        | Sauce Labs Backpack       |

@smoke
Scenario: Add items to cart by going to Details page of the products
    Given I login as standard user
    When I add the following items to the cart by going to Details page of each product
        | item_name                         |
        | Sauce Labs Backpack               |
        | Test.allTheThings() T-Shirt (Red) |
    Then the cart should contain the following items
        | item_name                         |
        | Sauce Labs Backpack               |
        | Test.allTheThings() T-Shirt (Red) |

@negative
@unstable
Scenario: Checkout with empty cart
    Given I login as standard user
    When I Click on the Shopping Cart Icon
    Then the cart should be empty after checkout
    And I should be Not be to able to checkout the empty cart