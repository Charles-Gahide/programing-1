#steps:
#ask for an input to choose word,

#make a live counter variable (3 lives)
#ask for a letter input
#if letter not in word > live counter -1
#if letter is in word > reveal it
#when there are no more empty spots "_" left, print "you win"
#if you are out of lives print "you lose"


# Choose the word to be guessed
word = input("Gamemaster, secretly type in the word you want them to guess: ")
print("\n"*50)


# Convert the word to a row of underscores
hidden_word = "_" * len(word)
lives = 5

print(hidden_word)
print(f"You have {lives} lives")

while lives > 0 and "_" in hidden_word:
    guess = input("Guess a letter: ").lower()
    correct_guess = False
    updated_hidden = ""

    for i in range(len(word)):
        if word[i].lower() == guess:
            updated_hidden += word[i]
            correct_guess = True
        else:
            updated_hidden += hidden_word[i]

    hidden_word = updated_hidden  # Always update the visible word

    if correct_guess:
        print(hidden_word)
    else:
        lives -= 1
        if lives == 0:
            print(f"WRONG! Game over. The word was: {word}")
        else:
            print(f"WRONG! You have {lives} lives remaining")
            print(hidden_word)

if "_" not in hidden_word:
    print("🎉 You guessed the word!")

    
