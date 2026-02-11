Feature: Edit note

  Scenario: User edits existing note
    Given Notes API is running
    And at least one note exists
    When user sends edited note
    Then edited note is shown

  Scenario: User edit non-existent note
    Given Notes API is running
    When user sends edited non-existent note
    Then response status code is 404
