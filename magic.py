<<<<<<< HEAD
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
=======
def play_Again():
    while True:
        choice=input("DO you want to ask another question?(yes/no):").strip().lower()
        if choice == "yes":
            return True
        elif choice=="no":
            print("thanks for playing!good bye!")
            return False
        else:
            print("enter type 'yes' or 'no' ")
>>>>>>> feature4
def magic_8_ball():
    print("welcome")
    while True :
        question=get_Random_repo
        if question is None :
            break
        response=get_Random_repo
        display_response(response)
        if not play_Again():
            break
if __name__=="__main__":
    magic_8_ball