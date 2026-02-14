Feature: Getting all notes

  Scenario: User requests all existing notes
    Given Notes API is running
    And at least one note exists
    When user requests the list of their notes
    Then existing notes are sent to them

  Scenario: User requests all notes when there is none
    Given Notes API is running
    When user requests the list of their notes
    Then empty list is returned