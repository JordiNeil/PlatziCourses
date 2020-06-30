# -*- coding:utf-8 -*-
import random
#Imagenes para el juego
IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\ |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\ |
    /   |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\ |
    / \ |
        |
    =========''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computador',
    'teclado',
]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('------ * ------ * ------ * ------ * ------ * ------ * ------ ')

def random_word():
    return WORDS[random.randint(0,len(WORDS)-1)]

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0
    while True:
        display_board(hidden_word, tries)
        current_letter = str(input("Ingresa una letra: "))

        letter_indexes = []
        for idx in range(len(word)):
            if (word[idx] == current_letter):
                letter_indexes.append(idx)
        if (len(letter_indexes) == 0):
            tries += 1
            print('intentos: '+str(tries))
            if(tries == 6):
                display_board(hidden_word, tries)
                print('')
                print('Game Over! The correct word was: {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter            
            letter_indexes = []
        try:
            hidden_word.index('-')
        except ValueError:
            print('You Won! The word was: {}'.format(word))
            break

if __name__ == "__main__":
    print ('B I E N V E N I D O S  A L  A H O R C A D O')
    run()
