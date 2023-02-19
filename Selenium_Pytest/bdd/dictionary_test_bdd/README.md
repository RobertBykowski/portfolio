Feature: checking if the search in the dictionary (https://www.diki.pl/) works correctly
  As a user I want to check some word in the dictionary


  Scenario: Check the correct search for exist words
     Given User is on Diki online dictionary website
      When User fills in the search bar and submits it
      Then User can see correct word

-----------------------------------------------------
The test is done with the Behave library for Python.
-----------------------------------------------------

Printing detailed information about tests (e.g. logs):
behave -vv
or
Printing the test result in JSON format:
behave --format=json
