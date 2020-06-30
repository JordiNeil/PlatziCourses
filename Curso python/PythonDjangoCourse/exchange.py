# -*- coding:utf-8 -*-

def main():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte de pesos mexicanos a pesos colombianos')
    print('')
    
    amount = float(input("Ingresa la cantidad de pesos mexicanos que quieres convertir: "))
    result =  foreingExchangeCalculator(amount)
    print("${} pesos mexicanos equivalen a ${} pesos colombianos".format(amount,result))
    print('')

def foreingExchangeCalculator(amount):
    mxnToCop = 145.97
    return amount * mxnToCop
    

if __name__ == '__main__':
    main()