Feature: checking if the search in the dictionary works correctly
  As a user I want to check some words in the dictionary

Scenario Outline: Check the correct search for exist words
  Given User is on Diki online dictionary website
  When User fills '<word>' in the search bar and submits it
  Then User can see correct description for a word '<word>'
  Examples:
    | word   |
    | boy    | 
    | home   |
    | pies   |
    | kot    | 

-----------------------------------------------------
The test is done with the Behave library for Python.
-----------------------------------------------------