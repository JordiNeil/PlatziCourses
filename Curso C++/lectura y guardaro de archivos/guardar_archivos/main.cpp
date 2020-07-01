#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ofstream MyFile("GameData.txt");
    string PlayerName = "";

    if (MyFile.is_open()){
        MyFile << "Hola Jordi!" << endl;
        MyFile << "Estoy bien" << endl;
        cout << "Introduce el nombre de tu heroe" << endl;
        cin >> PlayerName;
        MyFile << PlayerName;
    }
    cout << endl;
    MyFile.close();

    ifstream MyFileRead("GameData.txt");
    string line;
    if (MyFileRead.is_open()){
        while(getline(MyFileRead, line)){
            cout << line << endl;
        }
    } else{
        cout << "No se pudieron cargar los datos del juego" << endl;
    }
    return 0;
}





