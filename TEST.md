## CONTENTS
* [Introduction](#introduction)
* [Testing Objectives](#testing-objectives)
* [Testing Methods](#testing-methods)
  * [Manual Testing](#manual-testing)
  * [Feedback and Iterative Improvement](#feedback-and-iterative-improvement)
  * [Automated Testing](#automated-testing)
* [Browser Testing](#browser-testing)
* [Google Sheets Testing](#google-sheets-testing)
* [Conclusion](#conclusion)

## Introduction

During the development of the Wordle game, thorough testing was conducted to ensure the application's functionality, usability, and robustness. This document outlines the various testing stages and methodologies used to validate each component of the game.

The Wordle game, developed using Python and integrated with Google Sheets, allows players to guess a 5-letter word within a set number of attempts, based on the selected difficulty level. The player's guesses and game outcomes are stored in Google Sheets, which also serves as the source for the list of valid words.

## Testing Objectives

The primary objectives of testing were to:

Validate the game's core functionality - ensuring that the word guessing mechanics, difficulty settings, and scoring system worked as intended.
Verify the integration with Google Sheets for storing high scores and fetching valid words.
Assess the user experience, including ease of navigation, clarity of instructions, and error handling.
Ensure compatibility across different operating environments.

## Testing Methods

### Manual Testing

A comprehensive series of manual tests were conducted to simulate various user interactions and scenarios. Key areas of focus included:

Gameplay Mechanics: Ensuring the game correctly accepts input, provides feedback, and adheres to the rules set for each difficulty level.
Google Sheets Integration: Verifying that the game correctly retrieves words from and records scores to Google Sheets.
Error Handling: Testing the game's response to invalid inputs or unexpected user actions.
User Interface: Checking for clarity of instructions, ease of use, and overall user experience.

Me and 2 of my friends that I have send the link to the game tested the game manually and the results are shown below.

| Feature                    | Expected Outcome                                                  | Testing Performed                                  | Result                                  | Pass/Fail |
|----------------------------|-------------------------------------------------------------------|----------------------------------------------------|-----------------------------------------|-----------|
| Game Initialization        | Game initializes with a welcome message and name prompt           | Started the game                                   | Welcome message and name prompt appear  | Pass      |
| Player Name Validation     | Reject names under 3 characters and prompt for re-entry           | Entered various name lengths                       | Incorrect names rejected, correct prompt | Pass      |
| Difficulty Selection       | Allows selection of difficulty and sets guess limit               | Selected each difficulty level                     | Correct guess limit set for each level   | Pass      |
| Word Guessing              | Accepts valid 5-letter words and provides feedback                 | Entered various valid and invalid words            | Valid words accepted, feedback provided  | Pass      |
| Guess Limit Functionality  | Game ends after reaching max guesses for difficulty               | Guessed until reaching the limit                   | Game ended after max guesses             | Pass      |
| High Score Functionality   | Records and displays high scores correctly                        | Completed games and checked high score list        | High scores recorded and displayed       | Pass      |
| Game Restart               | Option to play again or return to main menu after game ends       | Selected options after game completion             | Correct navigation after game            | Pass      |
| Input Error Handling       | Display error for invalid inputs and allows correction            | Entered invalid inputs and corrected               | Error displayed, correction allowed      | Pass      |
| Data Persistence           | Scores and words persist across sessions                          | Restarted game, checked scores and word list       | Data persisted correctly                 | Pass      |
| User Interface Consistency | UI elements consistent and responsive throughout gameplay         | Interacted with various UI elements                | UI consistent and responsive             | Pass      |

### Automated Testing

Automated testing was not the primary focus due to the nature of the project. However, the code was regularly checked against PEP 8 standards to ensure code quality and readability. No errors in the final project.

* [pep8 Linter CI](https://pep8ci.herokuapp.com/#) - Used for checkig the code against pep8 format errors

## Browser Testing

The game was tested in various browser environments to ensure consistent performance. The primary browsers used for testing included:

Chrome
Firefox
Edge

## Google Sheets Testing

With Google Sheets being an integral part of the game's functionality, several tests were conducted to ensure reliable data retrieval and storage. These tests included:

Adding and retrieving words from the word list.
Recording and fetching high scores.

## Conclusion
The testing process was critical in refining the Wordle game, ensuring its reliability, and enhancing the user experience. Continuous testing and feedback played a significant role in achieving a robust and enjoyable game.

