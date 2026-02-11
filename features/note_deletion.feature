Feature: Deletion of a note

  Scenario:
    Given Notes API is running
    And at least one note exists
    When user deletes the note
    Then the note is deleted

  Scenario:
    Given Notes API is running
    When user deletes non-existent note
    Then response status code is 404