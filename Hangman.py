import random
import Hangman_art
import Hangman_wordlist
from os import system
from time import sleep

# chosing random word from the wordlist
chosen_word = random.choice(Hangman_wordlist.words)
chosen_word = chosen_word.lower()
#if you want to develop the game uncomment the above line for ease of testing
#print(chosen_word)
underscore = []
lives = 6
hangmanpic = 0

system("cls")

print(Hangman_art.logo)

#Making underscores as many as letters in the word.
for letter in chosen_word:
    underscore+="_"
while(True):
     
    print(underscore)
    guess = input("Enter your guess: ").lower()
            
    num = 0
    
    if guess in underscore:
        print("Guess already in word")
        continue
        
    for position in chosen_word:

        if position == guess:
            underscore[num] = guess
        num+=1
    if guess not in chosen_word:
        lives-=1
        print(f"\nYou have guessed wrong letter, you have only {lives} lives remaining")
        hangmanpic+=1
            
    if "_" not in underscore:
        print("You have won")
        print(Hangman_art.trophy)
        break
    elif lives == 0:
        print(Hangman_art.stages[6])
        print(Hangman_art.gameover)
        print(f"The word was {chosen_word}")
        break
    print(Hangman_art.stages[hangmanpic])