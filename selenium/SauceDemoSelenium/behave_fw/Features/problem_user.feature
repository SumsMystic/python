Feature: As a problem user, I want to verify broken functionality in the application

@problemuser @productremovechecks
Scenario: Verify remove product functionality of the application
    Given I login as problem user
    When I add the following items to the cart
        | item_name                 |
        | Sauce Labs Backpack       |
        | Sauce Labs Fleece Jacket  |
    And I remove the following items from the cart
        | item_name                 |
        | Sauce Labs Fleece Jacket  |
    Then the remove button will not change status to add
    And the cart should show the following items
        | item_name                 |
        | Sauce Labs Backpack       |
        | Sauce Labs Fleece Jacket  |

@problemuser @shoppingitemimagechecks
Scenario: Verify image of the product in the cart
    Given I login as problem user
    When I check the image of the following items
    alt="Sauce Labs Bolt T-Shirt" class="inventory_item_img"
        | item_name                 |
        | Sauce Labs Backpack       |
        | Sauce Labs Fleece Jacket  |
    Then the images of the items should be displayed incorrectly


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