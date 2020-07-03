#include <iostream>
#include "Player.h"
#include "MapCell.h"

using namespace std;

int main()
{
    bool isGameOver = false;
    Player Hero;

    cout << "Inicial el Juego!" << endl;

    while(isGameOver == false){
        Hero.CallInput();
    }

    return 0;
}
