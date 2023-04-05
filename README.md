# Hangman

This is a Python code for a game of Hangman where the user is prompted to guess a movie title within a limited number of attempts. Here is a brief description of the code:

- The code imports two modules: random and sys.

- The game is implemented using a class called Hangman.

- The MOVIES_AND_HINTS dictionary inside the Hangman class holds movie names and their corresponding hints.

- The __init__ method initializes the game state, including the number of attempts and the selected movie.

- The displayed_string list in the __init__ method is a list of underscores and colons that will be replaced with correct guesses as the user plays the game.

- The guess_matcher method is the main game loop, which repeatedly calls get_guess, update_display, and update_attempts, and then checks the game status with check_game_status.

- The get_guess method prompts the user for a guess and returns it, after performing some input validation.

- The update_display method updates the displayed_string list with the user's correct guess.

- The update_attempts method decrements the attempts counter and displays a hint when appropriate.

- The show_hint method prompts the user for whether they want a hint and returns the hint corresponding to the movie if the user agrees.

- The check_game_status method checks if the game has ended and prints the appropriate message. If the game has ended, it prompts the user to play again.

- The play_again method prompts the user for whether they want to play again and either resets the game state or exits the program, depending on the user's input.

- Finally, the code creates an instance of the Hangman class and calls the guess_matcher method to start the game.
