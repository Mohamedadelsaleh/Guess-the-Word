import random

while True:
    name = input("Enter Your Name :  ").strip()
    if name.isalpha():
        name = str(name)
        break

print(f"Good Luck {name}")

words = ['football', 'basketball', 'handball', 'volleyball', 'soccer', 'tennis', 'baseball', 'swimming', 'boxing',
         'skiing', 'cricket', 'rugby', 'bowling', 'surfing', 'karate', 'cycling', 'fishing', 'gymnastics',
         'judo', 'kickboxing']

word = random.choice(words)
print("Your word has", len(word), "letters.")

print("Hint: Your Guessing Word is a Sport")
print("Guess the characters")

guesses = ''

turns = 7

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Win")

        print("The word is: ", word)
        break

    guess = input("guess a character:")

    guesses += guess

    if guess not in word:

        turns -= 1

        print("Wrong")

        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("Sorry,You Lose")
