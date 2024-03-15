import random
Hangman_arr=['''
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
  wordindex=random.randint(0,int(len(mainwords)-1))
  return word[wordindex]
def showfunc(wrong,correct,randomword):
  print(Hangman_arr[len(wrong)-1])
  print()
  print('Wrong words enter by user : ',end=' ')
  for letters in wrong:
    print(letters,end=' ')
  print() 
  print("Correct words : ",end="")
  blanks= '_' * len(randomword)
  for i in range(len(randomword)):
    if randomword[i] in correct:
      blanks=blanks[:i]+randomword[i]+blanks[i+1:]
  for letter in blanks:
    print(letter,end='')
  print()  
def guessfunc(already):
  while True:
    print('guess a letter')
    guess=input()
    guess=guess.lower()
    if len(guess)!=1:
      print('enter the single letter')
    elif guess in already:
      print('enter alphabet is  already guessed')
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
      print("enter valid alphabet")
    else:
      return guess

print("Welcome!!")      
wrong=''
correct=''
randomword=randomwords(mainwords)

endgame=False
while True:

  showfunc(wrong,correct,randomword)
  guess1=guessfunc(wrong+correct)
  if guess1 in randomword:
    correct=correct+guess1
    foundall=True
    for i in range(len(randomword)):
      if(randomword[i] not in correct):
        foundall=False
        break
    if foundall:
      print("You win")
      endgame=True
      print("Please give the feedback to the game")
      feedback=input()
      print("Thanks for the feedback")
      break
  else:
    wrong=wrong+guess1
    if len(wrong)==len(Hangman_arr)-1:


      showfunc(wrong,correct,randomword)
      print("Correct guesses is "+str(len(correct)) + "and wrong guesses is"+ str(len(wrong)))
      print("Try again chances are over")
      break
