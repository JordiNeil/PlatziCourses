# -*- coding:utf-8 -*-
    
def factorial(numero):
    if (numero == 0):
        return 1    
    return numero * factorial(numero-1)

if __name__ == "__main__":
    n = int(input('Ingrese el número a calcular el factorial: '))
    result = factorial(n)

    print ('El resultado es: '+ str(result))