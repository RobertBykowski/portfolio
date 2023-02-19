Feature: checking if the search in the dictionary works correctly
  As a user I want to check some word in the dictionary


  Scenario: Check the correct search for exist words
     Given User is on Diki online dictionary website
      When User fills in the search bar and submits it
      Then User can see correct word