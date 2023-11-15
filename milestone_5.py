
import random

class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in self.word]
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses =[]

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word ")
            for i, letter in enumerate (self.word):
                if self.word[i] == guess:
                    self.word_guessed[i]=guess            
            print(self.word_guessed)
            self.num_letters -= 1
            
                    
        else:
            print(f"Sorry {guess} is not in word.Try again")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left")
    
    def ask_for_input(self):
        #while True:
        guess = input("enter a letter: ")
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter.Please,enter a single alphabetical character")
        elif guess in self.list_of_guesses:
            print("You already tried that letter")
        else:
            self.list_of_guesses.append(guess)
            self.check_guess(guess)

def play_game(word_list):
    game = Hangman(word_list)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_lives !=0 and game.num_letters <= 0:
            print("Congratulations. You won the game!")
            break
        elif game.num_lives > 0:
            game.ask_for_input()

play_game(["mango","banana","pineapple","pear","orange"])
                  

