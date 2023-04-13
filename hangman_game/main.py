import random


def main():

    KEY_WORD = 'exit'
    HIDING_SYMBOL = '_'
    BEGIN_ASCII = ord('a')
    END_ASCII = ord('z')
    ORIGINAL_GUESSES = 6
    CHANGE_GUESS = 1
    END_GUESSES = 0
    words = list(map(str, open('./hangman_game/words.txt').read().split()))

    while True:
        word = random.choice(words)
        guesses = ORIGINAL_GUESSES
        open_letters = [HIDING_SYMBOL]*len(word)
        used_letters = []

        while HIDING_SYMBOL in open_letters and guesses > END_GUESSES:

            print(f'You have {guesses} tries left')
            print('Used letters: ', *used_letters)
            print('Word: ', *open_letters)
            letter = input('Guess a letter: ')
            print('\n')
            if ord(letter) > END_ASCII or ord(letter) < BEGIN_ASCII:
                print('Incorrect symbol. Try again')
                continue
            used_letters.append(letter)

            if letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        open_letters[i] = letter
            else:
                guesses -= CHANGE_GUESS

        if HIDING_SYMBOL in open_letters:
            print('Sorry, you lose :-(')
            print(f'The word was {word}')
        else:
            print(f'You guessed the word {word} !')

        continuation = input(f'Enter word {KEY_WORD} if you want to finish: ')
        if continuation == KEY_WORD:
            print('Goodbye!!')
            break
        else:
            print('\n')


if __name__ == '__main__':
    main()
