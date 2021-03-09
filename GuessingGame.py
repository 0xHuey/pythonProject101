
#Start with a variable to hold our secret word

secret_word = "Giraffe"

#variable to hold users input

guess = ""

#Setting limits on the amount of loops
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
#Setting limits on the amount of loops
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guessess, You lose!")
else:
    print("You win!")