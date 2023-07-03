
def guess_letters():
    word = 'EVAPORATE'
    display = ['_' for i in range(len(word))]
    print('Welcome to Hangman! \n' + " ".join(display))
    previous_guesses = []
    while True:
        guess = input('Guess your letter: ').upper()
        while guess in previous_guesses:
            guess = input('You already guessed that, try another: ').upper()
        if guess not in word:
            print('Incorrect!')
            previous_guesses.append(guess)
        elif guess in word:
            for i in range(len(word)):
                if guess == word[i]:
                    display[i] = guess
                    previous_guesses.append(guess)
            print(" ".join(display))
        if '_' not in display:
            print(f'\nYOU WON!\nYou found the word {word}')
            break

guess_letters()
