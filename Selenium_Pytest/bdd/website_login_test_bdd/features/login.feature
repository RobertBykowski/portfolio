Feature: sign in to e-mail account
  As a user I want to log in and check my e-mails

  Scenario: Log in with valid data
     Given User is on WSB website
      When User fills in the Sign In form and submits it
      Then User can see email list

