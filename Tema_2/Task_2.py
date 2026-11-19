import random

secret_number = random.randint(1, 100)

previous_guess = None

print("Guess the number between 1 and 100!")
print("You have 7 attempts.")

for attempt in range(1, 8):
    guess = int(input("Enter your guess: "))

    if guess == previous_guess:
        print("Warning: You already guessed this number!")

    previous_guess = guess

    if guess == secret_number:
        print("Correct!")
        print("You guessed the number in", attempt, "attempts.")
        break

    elif guess < secret_number:
        print("Too low.")

    else:
        print("Too high.")

else:
    print("You have used all 7 attempts.")
    print("The secret number was:", secret_number)