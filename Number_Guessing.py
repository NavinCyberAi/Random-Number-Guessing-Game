class game():
    def Display(self):
        self.Name=input("Enter Your Name:")
    def Guess(self):
        print("Welcome to the Random Number Guessing Game")
        print(f"👤 Player Name: {self.Name}")
        import random
        My_Number=random.randint(1,100)
        for i in range(1,11):
            try:
                Guess_Number=int(input("Enter the Guess number:"))
                if Guess_Number<1 or Guess_Number>100:
                    print("Try Again Type the Number Between (1 to 100)")
                elif Guess_Number>My_Number:
                    print("The Number is Greater than Guessing Nmuber")
                elif Guess_Number<My_Number:
                    print("The Number is Less than Guessing Nmuber")
                else:
                    print("Your Number is Correct ")
                    break
            except ValueError:
                print("Type only  Number not Letters ...")
        if Guess_Number==My_Number:
            print(f"Congratulation, Successfully Got the Secret Number {My_Number} And Your Attempt is {i}")
        else:
            print(f"Sorry Your Number is {Guess_Number} Not Correct And Your Attempt is {i}")
            print(My_Number ,"is correct answer")
Player=game()
Player.Display()
Player.Guess()
