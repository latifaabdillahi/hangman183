from milestone_2 import word
print(word)



# while True:
#     guess = input("enter a letter: ")
#     if len(guess) == 1 and guess.isalpha():
#         if guess in word:
#             print(f"Good guess! {guess} is in the word ")
#         else:
#             print(f"Sorry {guess} is not in word.Try again")
#     else:
#         print("Invalid letter. Please enter a single aphabetical character")


def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word ")
    else:
        print(f"Sorry {guess} is not in word.Try again")

def ask_for_input():
    while True:
        guess = input("enter a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        #check_guess(guess)

        else:
            print("Invalid letter. Please enter a single aphabetical character")
    check_guess(guess)

ask_for_input()
######### ask why check guess function isnt working outside 
# the while loop (becuase guess isnt  defined outside the loop)