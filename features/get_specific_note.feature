Feature: Get the note by its ID

  Scenario: Get a specific note by ID
    Given Notes API is running
    And at least one note exists
    When user requests this note
    Then it is shown to them

  Scenario:
    Given Notes API is running
    When user searches a note by non-existent ID
    Then response status code is 404