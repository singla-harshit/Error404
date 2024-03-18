import tkinter as tk
from tkinter import messagebox
import random

# Hangman graphics
Hangman_arr = ['''
  +---+
      |
      |
      |
      ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\\  |
 / \\  |
     ===''']

# List of words for the game
mainwords = 'sleeve fancade stress reform working busy writer forget beleive summer chance rabbit install damage error developer coder flight broken prince bother translater language mind life better india account monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork religion man women children master piece movie film photo'.split()


def random_word(word_list):
    return random.choice(word_list)


class HangmanGame:
    def _init_(self, master):
        self.master = master
        self.master.title("Hangman Game")

        # Rules button
        self.rules_button = tk.Button(master, text="Rules", command=self.display_rules, font=('Arial', 16))
        self.rules_button.pack()

        self.word = random_word(mainwords)
        self.remaining_guesses = len(Hangman_arr)
        self.correct_guesses = []
        self.incorrect_guesses = []

        # Hangman display
        self.hangman_display = tk.Label(master, text="", font=('Arial', 14))
        self.hangman_display.pack()

        # Correct and incorrect guesses
        self.correct_guesses_label = tk.Label(master, text="Correct guesses: ", font=('Arial', 14))
        self.correct_guesses_label.pack()

        self.incorrect_guesses_label = tk.Label(master, text="Incorrect guesses: ", font=('Arial', 14))
        self.incorrect_guesses_label.pack()

        # Guess entry
        self.guess_entry = tk.Entry(master, font=('Arial', 16))
        self.guess_entry.pack()

        # Guess button
        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess, font=('Arial', 16))
        self.guess_button.pack()

        # End Game button
        self.end_game_button = tk.Button(master, text="End Game", command=self.end_game, font=('Arial', 16))
        self.end_game_button.pack()

        # Play Again button
        self.play_again_button = tk.Button(master, text="Play Again", command=self.play_again, font=('Arial', 16),
                                            state=tk.NORMAL)
        self.play_again_button.pack()

        self.update_hangman_display()

    def display_rules(self):
        messagebox.showinfo("Rules", "The rules of Hangman are simple:\n"
                                     "1. Try to guess the word by entering one letter at a time.\n"
                                     "2. You have a limited number of guesses.\n"
                                     "3. Every incorrect guess adds a part to the hangman.\n"
                                     "4. Guess all the letters before the hangman is complete to win the game.")

    def update_hangman_display(self):
        hangman_index = len(Hangman_arr) - self.remaining_guesses
        self.hangman_display.config(text=Hangman_arr[hangman_index])
        if hangman_index == 5:
            
            messagebox.showinfo("Game Over", " you lost the game.")
            hangman_index = 5
            self.word = random_word(mainwords)
            self.remaining_guesses = len(Hangman_arr)
            self.correct_guesses = []
            self.incorrect_guesses = []
            self.correct_guesses_label.config(text="Correct guesses: ")
            self.incorrect_guesses_label.config(text="Incorrect guesses: ")
            self.play_again_button.config(state=tk.NORMAL)
            self.update_hangman_display()
            return

    def play_again(self):
        self.word = random_word(mainwords)
        self.remaining_guesses = len(Hangman_arr)
        self.correct_guesses = []
        self.incorrect_guesses = []
        self.correct_guesses_label.config(text="Correct guesses: ")
        self.incorrect_guesses_label.config(text="Incorrect guesses: ")
        self.play_again_button.config(state=tk.NORMAL)
        self.update_hangman_display()

    def check_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)  # Clear the entry

        if not guess.isalpha() or len(guess) != 1:
            messagebox.showerror("Error", "Please enter a single alphabetical character.")
            return

        if guess in self.correct_guesses or guess in self.incorrect_guesses:
            messagebox.showinfo("Info", f"You already guessed '{guess}'.")
            return

        if guess in self.word:
            self.correct_guesses.append(guess)
            self.correct_guesses_label.config(text=f"Correct guesses: {', '.join(self.correct_guesses)}")
            if set(self.word) <= set(self.correct_guesses):
                messagebox.showinfo("Congratulations", "Congratulations, you won!")
                self.play_again_button.config(state=tk.NORMAL)
        else:
            self.incorrect_guesses.append(guess)
            self.incorrect_guesses_label.config(text=f"Incorrect guesses: {', '.join(self.incorrect_guesses)}")
            self.remaining_guesses -= 1
            self.update_hangman_display()

    def end_game(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    hangman = HangmanGame(root)
    root.mainloop()


if __name__ == "_main_":
    main()