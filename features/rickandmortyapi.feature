Feature: API Testing in Rick and Morty

    Scenario: Get character count
        Given I set url to "https://rickandmortyapi.com/api/character"
        Then I should expect a "200" response
            And character count to "671"

    Scenario: Get location count
        Given I set url to "https://rickandmortyapi.com/api/location"
        Then I should expect a "200" response
            And location count to "108"

    Scenario: Get episodes count
        Given I set url to "https://rickandmortyapi.com/api/episode"
        Then I should expect a "200" response
            And episode count to "41"

    Scenario: Get all genderless characters that are alive
        Given I set url to "https://rickandmortyapi.com/api/character?gender=genderless&status=alive"
        Then I should expect a "200" response
            And alive genderless characters are "9"

    Scenario: Expect a character name
        Given I set url to "https://rickandmortyapi.com/api/character/1"
        Then I should expect a "200" response
            And character name is expected to be "Rick Sanchez"

    Scenario: Get Invalid character id
        Given I set url to "https://rickandmortyapi.com/api/character/777"
        Then I should expect a "404" response

    Scenario: Get how many episodes a character appeared
        Given I set url to "https://rickandmortyapi.com/api/character/88"
        Then I should expect a "200" response
            And "character" appeared in "n" episodes

    Scenario: Get how many characters appeared in an episode
        Given I set url to "https://rickandmortyapi.com/api/episode/1"
        Then I should expect a "200" response
            And "x" characters appeared in episode "y"