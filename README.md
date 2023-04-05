# Hangman

This is a Python code for a game of Hangman where the user is prompted to guess a movie title within a limited number of attempts. Here is a brief description of the code:

- The random and sys modules are imported at the beginning.
- A class Hangman is defined which encapsulates the methods for playing the game.
- A dictionary MOVIES_AND_HINTS is defined with movie titles as keys and values as lists containing year of release and genre.
- The constructor of the Hangman class initializes the number of attempts to 10, selects a random movie title from the MOVIES_AND_HINTS dictionary, and creates a list of - underscores and colons as placeholders for the letters of the movie title.
- The show_hint() method prompts the user to choose whether they want a hint or not. If yes, it returns the year of release of the movie title when the attempts remaining are 5, else it returns the genre of the movie.
- The get_guess() method prompts the user to guess a character or the whole title and returns the input.
- The update_display(guess) method updates the displayed string with the correctly guessed letter.
- The update_attempts() method decrements the number of attempts and shows a hint if attempts remaining are 5 or 2.
- The check_game_status() method checks if the game is won or lost and prompts the user to play again or exit.
- The play_again() method prompts the user to choose whether they want to play again or exit.
- The guess_matcher() method is the main game loop that calls the other methods to play the game.
- Finally, the Hangman class is instantiated and the guess_matcher() method is called to start the game.
