# -*- coding:utf-8 -*-

#   Author: Jordi Neil Sánchez Angarita

""" Codigo para búsqueda binaria en lista ordenada """

def binarySearch(numbers, numberToFind, low, high):
    
    if(low>high):
        return False

    mid = int((low + high) / 2)

    if (numbers[mid] == numberToFind):
        return True
    elif (numbers[mid] > numberToFind):
        return binarySearch(numbers, numberToFind, low, mid - 1)
    else:
        return binarySearch(numbers, numberToFind, mid + 1, high)


if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]
    numberToFind = int(input("Ingrese un número: "))
    result = binarySearch(numbers, numberToFind, 0, len(numbers) - 1)

    if (result):
        print ('El número sí está en la lista')
    else:
        print('El número no está en la lista')

