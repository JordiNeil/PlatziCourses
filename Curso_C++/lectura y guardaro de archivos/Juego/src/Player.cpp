#include "Player.h"
#include <iostream>

using namespace std;

Player::Player()
{
    x=1;
    y=1;
    //ctor
}
void Player::CallInput(){
    char UserInput = ' ';
    cin >> UserInput;

    switch(UserInput){
    case 'a':
        x -= 1;
        cout << "El jugador se mueve a la izquierda" << endl;
        break;
    case 'd':
        x += 1;
        cout << "El jugador se mueve a la derecha" << endl;
        break;
    case 'w':
        y += 1;
        cout << "El jugador se mueve a la arriba" << endl;
        break;
    case 's':
        y -= 1;
        cout << "El jugador se mueve a la abajo" << endl;
        break;

    }

    cout << "Mi jugador esta en las coordenadas: "<< x << "," << y << endl;
}
