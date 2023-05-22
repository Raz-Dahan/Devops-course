from random import choice

file = open("C:\\Users\\razda\\OneDrive\\Documents\\ParcticePython.org\\30. Pick Word - sowpods.txt", "r")
data = file.read().split('\n')


def guess_letters():
    word = choice(data)
    display = ['_' for i in range(len(word))]
    print('Welcome to Hangman! \n' + " ".join(display))
    previous_guesses = []
    mistakes = 0
    while mistakes != 6:
        guess = input('Guess your letter: ').upper()
        while guess in previous_guesses:
            guess = input('You already guessed that, try another: ').upper()
        if guess not in word:
            previous_guesses.append(guess)
            mistakes += 1
            tries_left = 6 - mistakes
            if tries_left == 0:
                print(f'Incorrect!\n\nYOU LOST!\nThe word was {word}')
                draw(mistakes)
                is_restart = input('Do you want to play again(y/n)? ').lower()
                if is_restart == 'y':
                    restart_game()
                else:
                    break
            else:
                print(f'Incorrect!\nYou have {tries_left} tries left')
                draw(mistakes)
        elif guess in word:
            for i in range(len(word)):
                if guess == word[i]:
                    display[i] = guess
                    previous_guesses.append(guess)
            print(" ".join(display))
        if '_' not in display:
            print(f'\nYOU WON!\nYou found the word {word}')
            is_restart = input('Do you want to play again(y/n)? ').lower()
            if is_restart == 'y':
                restart_game()
            else:
                break

def draw(stage):
    stages = [
        """
           -----
          |     |
          |
          |
          |
          |
        """,
        """
           -----
          |     |
          |     O
          |
          |
          |
        """,
        """
           -----
          |     |
          |     O
          |     |
          |
          |
        """,
        """
           -----
          |     |
          |     O
          |    /|
          |
          |
        """,
        """
           -----
          |     |
          |     O
          |    /|\\
          |
          |
        """,
        """
           -----
          |     |
          |     O
          |    /|\\
          |    /
          |
        """,
        """
           -----
          |     |
          |     O
          |    /|\\
          |    / \\
          |
        """
    ]
    print(stages[stage])

def restart_game():
    guess_letters()

guess_letters()
