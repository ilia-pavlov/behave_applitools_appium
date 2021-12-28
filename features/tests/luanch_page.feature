# Created by iliapavlov at 4/16/21
Feature: Lunch page flow

  Scenario: User open info screen and returned to Welcome screen.
    Given tap on Get started button on launch page
    Then Tap on info button
    Then Tap on Cancel cta
    Then observe Welcome! screen

  Scenario: User open info screen and returned to Welcome screen.
    Given tap on Get started button on launch page
    Then Tap on info button
    Then Tap on Cancel cta
    Then observe NICE! screen
