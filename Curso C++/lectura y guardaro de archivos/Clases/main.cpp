#include <iostream>

using namespace std;

class Dog
{
public:
    string mBark;
    Dog(string name, string BarkType){
        mName = name;
        mBark = BarkType;
    }

    string GetName(){
        return mName;
    }

    void setName(string NewName){
        mName = NewName;
    }

    void Ladrar(){
        cout << mBark << endl;
    }
private:
    string mName;
};

int main()
{
    Dog perroUno("Peeerro1", "Berk");
    perroUno.setName("Perroo2");

    Dog perroDos("Comodoro", "Woof");
    cout << perroUno.GetName() << endl;
    cout << perroDos.GetName() << endl;

    perroUno.Ladrar();
    perroDos.Ladrar();

    return 0;
}
