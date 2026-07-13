questions = [
    "Which planet in our solar system is known as the 'Red Planet'?",
    "What is the capital city of Australia?",
    "In which year did the RMS Titanic sink during its maiden voyage?",
    "Who wrote the famous play Romeo and Juliet?",
    "What does 'HTTP' stand for in computing?"
]

options = [
    ['A. Venus', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
    ['A. Sydney', 'B. Melbourne', 'C. Canberra', 'D. Perth'],
    ['A. 1905', 'B. 1912', 'C. 1918', 'D. 1923'],
    ['A. Charles Dickens', 'B. Jane Austen', 'C. Mark Twain', 'D. William Shakespeare'],
    ['A. HyperText Transfer Protocol', 'B. HyperText Transmission Process', 'C. Hyperlink Transfer Technology',
     'D. HyperText Type Protocol']
]

answers = ['B', 'C', 'B', 'D', 'A']
guesses = []
score = 0

# enumerate() gives us both the index (question_num) and the item (question)
for question_num, question in enumerate(questions):
    print('-------------------------')
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter your guess: ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print('Your guess is correct!')
    else:
        print('Your guess is incorrect!')
        print(f'{answers[question_num]} is the correct answer!')

print('-------------------------')
print("         RESULTS         ")
print('-------------------------')

print('Answers: ', end='')
for answer in answers:
    print(answer, end=' ')
print()

print("Guesses: ", end='')
for guess in guesses:
    print(guess, end=' ')
print()

# Calculate percentage and format it with an f-string
score_percentage = int(score / len(answers) * 100)
print(f'Your score: {score_percentage}%')