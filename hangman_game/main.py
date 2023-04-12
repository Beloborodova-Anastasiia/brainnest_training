import random


def main():

    words = list(map(str, open('words.txt').read().split()))
    KEY_WORD = 'exit'
    UNDERLINE = '_'
    BEGIN_ASCII = ord('a')
    END_ASCII = ord('z')

    while True:
        word = random.choice(words)
        guesses = 6
        open_letters = [UNDERLINE]*len(word)
        used_letters = []

        while UNDERLINE in open_letters and guesses > 0:

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
                guesses -= 1
            
        if UNDERLINE in open_letters:
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