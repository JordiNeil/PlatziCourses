# -*- coding:utf-8 -*-

def run(cadena):
    letrasPrevias = []
    letrasRepetidas = []
    for letra in cadena:
        for letra2 in letrasPrevias:
            if (letra == letra2):
                letrasRepetidas.append(letra)

        letrasPrevias.append(letra)    
    letrasNoRepetidas = list(cadena)
    for letra3 in letrasRepetidas:
        for letra4 in letrasNoRepetidas:
            if(letra3 == letra4):
                letrasNoRepetidas.remove(letra4)
    if (len(letrasNoRepetidas)>0):
        return letrasNoRepetidas[0]
    else:
        return '_'


if __name__ == "__main__":
    print('ENCONTRAR PRIMERA LETRA QUE NO SE REPITE')
    cadena = str(input("Inserte la cadena a analizar: "))
    letra = run(cadena)
    print('La primera letra que no se repite es: {}'.format(letra))