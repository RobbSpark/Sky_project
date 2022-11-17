Feature: Add a product to the basket
  As a consumer, I want to add a product to the shopping basket


  Scenario Outline: I can see success message in the basket for multiple products
    Given I open product page "<link>"
    When I add the product to the basket
    Then I see success message

    Examples:
      | link                                                                             |
      | http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/              |
      | http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/ |