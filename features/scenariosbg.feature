
Feature: # Enter feature name here
  # Enter feature description here


  Background:
    Given I open product page "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    When I add the product to the basket

  Scenario: I can see success message in the basket
    Then I see success message


  Scenario: Product should be added to the basket
    Then I see message of product added


  Scenario: Product price should match with basket total
    Then I see that basket total matches product price