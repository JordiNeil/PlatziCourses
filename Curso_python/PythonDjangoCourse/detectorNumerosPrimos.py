# -*- coding:utf-8 -*-

def esPrimo(numero):
    if(numero < 2):
        return False
    elif(numero == 2):
        return True 
    elif (numero >2 and numero % 2 == 0):
        return False
    else:
        for i in range(3, numero):
            if (numero % i == 0):
                return False        
    return True
     

def main():
    numero = int(input("Ingrese el número a evaluar: "))
    result = esPrimo(numero)

    if (result):
        print ('Tu número es primo')
    else:
        print('Tu número no es primo')

if __name__ == "__main__":
    main()