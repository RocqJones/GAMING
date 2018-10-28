#This plays many games with (y/n)
import random

random_number = random.randint(1,10)
guess = None

while True:    
    #guess = int(input("Pick any number from 1 to 10: "))
    #the try and except block will make sure no errors of input
    try:
        guess = int(input("Pick any number from 1 to 10: "))
    except:
        print("Enter a valid number")
    else:       
        if guess < random_number:
            print("NUMBER TOO LOW!")
        elif guess > random_number:
            print("NUMBER TOO HIGH!")
        else:
            print(f"YOU GOT IT! \nThe number was {random_number}")
            play_again = input("Do you want to play again? (y/n)")
            if play_again == "y":
                random_number = random.randint(1,10)
                guess = None
            else:
                print("Thank you for playing!")
                break
