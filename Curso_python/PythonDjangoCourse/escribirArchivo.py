# -*- coding:utf-8 -*-

def run():
    counter = 0
    with open('numeros.txt', 'r') as f:
        for line in f:
            counter += line.count('Jordi')

    print ('Jordi se encuentra {} veces en el texto'.format(counter))
            

if __name__ == "__main__":
    run()