<<<<<<< HEAD
<<<<<<< HEAD
def get_user_guess():
    while True :
        try:
            guess=int(input("Enter your guess(1-100):"))
            if 1<=guess<=100:
                return guess
            else:
                print("Enter a number between 1 and 100.")
        except ValueError:
            print("invalid input! Please enter a number.")
=======
import random
responses=[
"yes,definitely!",
"No,not now","Ask Again Later",
"It is certain",
"Very doubt ful",
"Out look is good",
"Better not tell you now",
"concentrate and ask again"
]
def get_Random_repo():
    return random.choice(responses)
>>>>>>> feature2
=======
def display_response(response):
    print("\nthe Magic ball says:",response,"\n")
>>>>>>> feature3
