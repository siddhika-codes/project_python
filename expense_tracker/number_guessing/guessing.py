# Project 4 — Number Guessing Game
secret_no = 23

attempts = 0

while True:
    guess_no = int(input("guess the number :"))
    attempts += 1
    if guess_no == secret_no:
        print("You got it!")
        break
    elif guess_no < secret_no:
        print("Too low! Try again")
    elif guess_no > secret_no:
        print("Two high! Try again")


print("No. of Attempts are :", attempts)
