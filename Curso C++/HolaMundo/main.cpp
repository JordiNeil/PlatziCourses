#include <iostream>
#include <fstream>

using namespace std;

void drawnMap(int heroPosX, int heroPosY, char gameMap[5][5]){
    for (int i = 0; i<5;i++){

            for (int j = 0; j<5;j++){
                if (i!= heroPosY){
                    cout <<gameMap[j][i];
                }else{
                    if (j != heroPosX){
                        cout << gameMap[j][i];
                    }else{
                        cout << 'H';
                    }
                }
            }
        cout << endl;
    }
}

int main()
{
    int heroPosX = 1;
    int heroPosY = 1;
    bool gameOver = false;
    char input = ' ';
    char gameMap[5][5] =
    {
        {'1','1','1','1','1'},
        {'1','1','1','1','1'},
        {'1','1','1','1','1'},
        {'1','1','1','1','1'},
        {'1','1','1','1','1'},
    };
    drawnMap(heroPosX, heroPosY, gameMap);

    while(!gameOver){
        cin >> input;
    if (input == 'd'){
        heroPosX++;
    }else if (input == 'a'){
        heroPosX--;
    }else if (input == 'p'){
        gameOver = true;
    }else if (input == 'w'){
        heroPosY--;
    }else if (input == 's'){
        heroPosY++;
    }
    drawnMap(heroPosX, heroPosY, gameMap);
    }


    return 0;
}
