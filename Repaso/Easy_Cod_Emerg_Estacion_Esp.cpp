#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;
    for (char &c : s) {
        if (c == '*') c = '0';
    }
    cout << s << endl;
    return 0;
}
/*Verificación:
Entrada: 1*0*1* → Salida: 100010
(Cualquier entrada con '*' se reemplaza por '0')*/