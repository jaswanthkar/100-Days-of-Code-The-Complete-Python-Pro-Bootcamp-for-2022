import random
logo=""" """
number = random.randint(1,100)
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level=="easy":
    n=10
elif level=="hard":
    n=5
print("This is a number guessing game, Guess anything between 1 and 100")
while(n>0):
    print(f"You have {n} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess==number:
        print("Correct guess")
        break
    else:
        if n==1:
            print("Out of Moves")
        else:
            if guess>number:
                print("Too high. \nGuess again.")
            elif guess<number:
                print("Too Low. \nGuess again.")
    n-=1
