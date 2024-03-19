Project Title : Creating Hangman Game

Description :
Hangman is a game where one player thinks of a word and the other player has to guess it letter by letter. For every wrong guess, a part of a stick figure is drawn. The game continues until the word is guessed correctly or the stick figure is completed . If the stick figure gets completed, then it means that you have used all your chances to guess and losses the game. The player must guess the word before losing all the chances(or before the hangman gets fully drawn).

Team Members :

Harshit Singla(2310990685) - Project Manager
Herish Kumar(2310990688) - Developer
Kushal Bansal(2310990721) - Tester  

Roles :

Harshit Singla : Assigning Tasks, Oversees project management and Ensures submission 
Herish Kumar : Designing the Game Logic, Develops functionalities and Implementing User Interface
Kushal Bansal : Ensures functionality, Run test cases to uncover defects or inconsistencies

Features :
Word Selection: Randomly select a word from a predefined list
Display Word: Represent the selected word with dashes to hide its letters.
Validate Input: Ensure that the user's input is a single letter and hasn't been guessed before.
Game Loop: Allow the player to continue guessing until they win or lose, with the option to play again.
Score Tracking: Keep track of the player's score based on the number of correct guesses and provide feedback at the end of each game.
Difficulty Levels: Offer different difficulty levels, such as easy (fewer letters) or hard (longer words).


Tests by Tester :-

In version 1.0
Test Cases :-
	Case 1:
	Wrong words enter by user : a m y o
	Correct words :newt
	You win
	Please give the feedback to the game
	Thank for the feedback

	Case 2:
	Wrong words enter by user : t s c g n w
	Correct guesses are 1and wrong guesses are 6
	Try again chances are over

PROBLEMS TO SOLVE:

      1. Should add Play Again feature.
      2. In wrong guess, number of correct and wrong guesses are printed but Hangman not get complete.
      3. Should add hint feature for making easy and for faster imagining.

In version 2.0
Test Cases :-
	Case 1:
	Wrong words entered by user: 
	Correct words: b e _ _ e r
	Game Over :- Sorry, you lost.

	Case 2:
	Wrong words entered by user: a, e, n
	Correct words: s l o t h
	Congratulations, you won!
	
Problems Resolved :-
      1. Added Play Again Feature.
      2. Modified its Display interface and added a Guess Button.

Problems to solve :-
      1. Guess Button not working automatically after entering alphabet.
      2. Display the correct guess alphabet on next guess.
      3. Can add a display for showing rules of game.
      4. Game is running still after lossing it.

In version 3.0
Test Cases :-
	Case 1:
	Correct guesses: a
	Incorrect guesses: e,r,x,z,q
	Game Over:-you lost the game

	Case 2:
	Correct guesses: r,a,t
	Incorrect guesses: b,m
	Congratulations, you won!

Problems Resolved:
      1. Guess Button works automatically.
      2. Display the alphabet whether wrong or correct after entering.
      3. Added a rule book on top for instructions about game.
      4. New Game will start automatically after loosing the game.
      5. Added End game button to end the game.

The Hangman game has several uses beyond just being a fun pastime. It can be used as an educational game to help learners improve their vocabulary and spelling skills. It is particularly useful for language learners as it allows them to practice spelling and expand their vocabulary in a fun and interactive way. It has been adapted into digital formats, including mobile apps and online games.