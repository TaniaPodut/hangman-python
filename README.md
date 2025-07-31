# Hangman Game in Python

This is a simple command-line implementation of the classic **Hangman** game (*Spânzurătoarea*), written in Python.

The game randomly selects a word from a predefined list, and the player must guess the word one letter at a time. The player has 6 attempts to guess the word correctly before the game ends.

---

## Features

- Random word selection
- Tracks guessed letters
- Feedback on correct and incorrect guesses
- Limited to 6 failed attempts
- Romanian interface

---

## Example Output

```text
Bine ai venit la jocul Spânzurătoarea!
Cuvântul de ghicit este: _ _ _ _ _ _

Introdu o literă: a
Bine ai ghicit!
Progres: _ a _ _ _ _

Introdu o literă: z
Litera nu se află în cuvânt! Mai ai 5 încercări.
