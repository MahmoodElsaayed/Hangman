import random
import sys


class Hangman:
    MOVIES_AND_HINTS = {
        "Detective Conan: Scarlet Bullet": ["2021", "anime"],
        "Star Wars: The Rise of Skywalker": ["2019", "science fiction"],
        "The Godfather": ["1972", "crime"],
        "The Shawshank Redemption": ["1994", "drama"],
        "The Lord of the Rings: The Fellowship of the Ring": ["2001", "fantasy"],
    }


    def __init__(self):
        self.attempts = 10
        self.selected_movie = random.choice(list(Hangman.MOVIES_AND_HINTS.keys()))
        self.displayed_string = ["_" if not(char.isspace() or char == ":") else char for char in self.selected_movie]


    def show_hint(self):
        while True:
            user_choice = input(">>> want a hint(y/n)? ").strip().lower()
            if user_choice in ["y", "yes"]:
                if self.attempts == 5:
                    return f"\nReleased in: {Hangman.MOVIES_AND_HINTS[self.selected_movie][0]}"
                else:
                    return f"\nGenre: {Hangman.MOVIES_AND_HINTS[self.selected_movie][1]}"
            elif user_choice in ["n", "no"]:
                return "You don't want to? ok ¯\_(ツ)_/¯ "
            else:
                print(f"'{user_choice}' isn't an available option. available: [y, yes, n, no]")


    def get_guess(self):
        while True:
            print(f"\n", *self.displayed_string, end="\n\n")
            user_guess = input(f"Guess a character or the whole title ({self.attempts} chances left): ").strip().lower()
            if user_guess:
                return user_guess
            else:
                print("You can't leave the answer field empty. Please input a valid answer")


    def update_display(self, guess):
        index = self.selected_movie.lower().find(guess)
        while index != -1:
            self.displayed_string[index:index+len(guess)] = guess
            index = self.selected_movie.lower().find(guess, index+1)


    def update_attempts(self):
        self.attempts -= 1
        if self.attempts == 5 or self.attempts == 2:
            print(self.show_hint())


    def check_game_status(self):
        if "_" not in self.displayed_string:
            print(f"\n", *self.displayed_string, "\nYou won ◝(ᵔᵕᵔ)◜\n")
            self.play_again()
        elif self.attempts == 0:           
            print("\nYou lost ( • ᴖ • ｡)\n")
            self.play_again()


    def play_again(self):
        while True:
            user_choice = input("Play again (y/n)? ").strip().lower()
            if user_choice in ["y", "yes"]:
                self.__init__()
                self.guess_matcher()
            elif user_choice in ["n", "no"]:
                sys.exit("\nThanks for playing ^_^")
            else:
                print(f"'{user_choice}' isn't an available option. available: [y, yes, n, no]")


    def guess_matcher(self):
        while True:
            guess = self.get_guess()
            self.update_display(guess) if guess in self.selected_movie.lower() else self.update_attempts()
            self.check_game_status()


hangman = Hangman()
print(hangman.guess_matcher())