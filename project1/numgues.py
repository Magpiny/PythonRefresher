# Number guessing game in python
import random

def number_guessing():
    # our random number
    system_number = random.randint(0, 10)

    # get user number
    user_number = int(input("Enter an integer number! : "))

    # Keep the program going as long as the answer is wrong
    while(user_number != system_number):
        # generate random numbers
        system_number = random.randint(0, 10)
        print(system_number)

        #user guessed number
        user_number = int(input("Enter an integer number! : "))

        if(user_number!=system_number):
            print("Wrong guess Try Again! ")
            print(f"The correct number was { system_number } but you gave us { user_number }")

        #if(user_number==system_number):
            #break
        
    else:
        print("CONGRATULATIONS! You win!")

number_guessing()

