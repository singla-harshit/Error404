import tkinter as tk
from tkinter import messagebox
import random

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
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
      |
     ===''']

mainwords = 'sleeve fancade stress reform working busy writer forget beleive summer chance rabbit install damage error developer coder flight broken prince bother translater language mind life better india account monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork religion man women children master piece movie film photo'.split()


def randomwords(word):
    wordindex = random.randint(0, int(len(mainwords) - 1))
    return word[wordindex]


def showfunc(wrong, correct, randomword):
    display_text = Hangman_arr[len(wrong) - 1]
    display_text += '\n\nWrong words entered by user: ' + ', '.join(wrong)
    display_text += '\nCorrect words: '
    blanks = '_' * len(randomword)
    for i in range(len(randomword)):
        if randomword[i] in correct:
            blanks = blanks[:i] + randomword[i] + blanks[i + 1:]
    display_text += ' '.join(list(blanks))
    return display_text


def guessfunc(already):
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) != 1:
            print('Enter a single letter.')
        elif guess in already:
            print('The letter is already guessed.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Enter a valid alphabet.")
        else:
            return guess


def play_again():
    global wrong, correct, randomword
    wrong = ''
    correct = ''
    randomword = randomwords(mainwords)
    hangman_display.config(text=showfunc(wrong, correct, randomword))
    play_again_button.config(state=tk.DISABLED)


def check_guess():
    global wrong, correct
    guess = guess_entry.get().lower()
    if len(guess) != 1 or not guess.isalpha():
        messagebox.showerror("Error", "Please enter a single alphabetical character.")
        return

    if guess in wrong or guess in correct:
        messagebox.showinfo("Info", f"You already guessed '{guess}'.")
        return

    if guess in randomword:
        correct += guess
    else:
        wrong += guess
        hangman_display.config(text=showfunc(wrong, correct, randomword))
        if len(wrong) == len(Hangman_arr) - 1:
            messagebox.showinfo("Game Over", "Sorry, you lost.")
            play_again_button.config(state=tk.NORMAL)
            return

    if set(randomword) <= set(correct):
        messagebox.showinfo("Congratulations", "Congratulations, you won!")
        play_again_button.config(state=tk.NORMAL)


root = tk.Tk()
root.title("Hangman Game")

wrong = ''
correct = ''
randomword = randomwords(mainwords)

hangman_display = tk.Label(root, text=showfunc(wrong, correct, randomword), font=('Arial', 14))
hangman_display.pack()

guess_entry = tk.Entry(root, font=('Arial', 16))
guess_entry.pack()

guess_button = tk.Button(root, text="Guess", command=check_guess, font=('Arial', 16))
guess_button.pack()

play_again_button = tk.Button(root, text="Play Again", command=play_again, font=('Arial', 16), state=tk.DISABLED)
play_again_button.pack()

root.mainloop()