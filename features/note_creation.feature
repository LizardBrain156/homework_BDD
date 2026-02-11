Feature: Note creation

  Scenario Outline: User posts a valid note
    Given Notes API is running
    When user posts a valid note with title "<title>" and content "<content>"
    Then response status code is 200

    Examples:
      | title       | content                    |
      | Pet a cat   | Don't forget to pet a cat  |
      | 12345       | 54321                      |
      | Погладить кота | Не забыть погладить кота |


  Scenario: User posts an invalid note
    Given Notes API is running
    When user posts an invalid note
    Then response status code is 422
