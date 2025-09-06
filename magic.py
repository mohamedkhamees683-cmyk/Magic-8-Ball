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