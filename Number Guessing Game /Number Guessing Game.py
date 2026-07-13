import random

low=1
high=100
answer=random.randint(low,high) #Picks a random number between 1 and 100
guesses=0
print("Guess the number")
print(f'Select a number between {low} and {high}')
while True:
    guess=(input("Enter your guess: "))
    if guess.isdigit(): #Checks whether the number is a digit or not
        guess=int(guess) #Type casting it into integer
        guesses+=1
        if guess <low or guess >high:
            print("Your guess is incorrect")
            print(f'Select a number between {low} and {high}')
        elif answer<guess:
            print("Your guess is too high")
        elif answer>guess:
            print("Your guess is too low")
        else:
            print(f'Correct!, you guessed {guess}')
            print(f'Number of guesses: {guesses}')
            break # breaks the loop when the correct answer is guessed
    else:
        print("Invalid input")
        print(f'Select a number between {low} and {high}')

