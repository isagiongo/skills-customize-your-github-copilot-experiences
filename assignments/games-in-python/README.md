
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build an interactive Hangman game in Python that uses strings, loops, conditionals, and user input to guess a hidden word.

## 📝 Tasks

### 🛠️ Create the game engine

#### Description
Implement the core Hangman gameplay so the program selects a word, accepts single-letter guesses, and updates the hidden word display.

#### Requirements
Completed program should:

- Randomly select a hidden word from a predefined list
- Accept one letter guess at a time from the player
- Reveal correct letters and keep unknown letters as `_`
- Track and display remaining incorrect guesses
- Avoid counting duplicate guesses more than once

### 🛠️ Add game flow and feedback

#### Description
Add win/lose conditions, player feedback after each turn, and a final result message at the end of the game.

#### Requirements
Completed program should:

- End when the player guesses the full word
- End when the player runs out of allowed attempts
- Display a win message that includes the completed word
- Display a lose message and reveal the hidden word
- Show the current word state and guessed letters after each guess
