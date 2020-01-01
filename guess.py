import random
print("Welcome to the guess game...\nYou will have 6 chance to find the guessed number...\nEnjoy the game")
secretNumber = random.randint(1,25)
chance = 0
while True:
    guess = int(input("Guess the number : "))
    if guess < secretNumber:
        print("You guess number is to low... ")
    elif guess > secretNumber:
        print("You guess number is to high...")
    elif guess == secretNumber:
        print("Awsomeeeee\nYou find the number...God Job...")
    chance += 1
    if chance == 6:
        print("Sorry you could not find it and you ouf of you chance try it next time...")