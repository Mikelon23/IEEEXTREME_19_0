#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> values(n);
    vector<int> positive_values;
    
    // Leer valores y filtrar positivos
    for (int i = 0; i < n; i++) {
        cin >> values[i];
        if (values[i] > 0) {
            positive_values.push_back(values[i]);
        }
    }
    
    if (positive_values.empty()) {
        cout << "0 0" << endl;
        return 0;
    }
    
    // Calcular promedio (redondeado hacia abajo)
    int sum = 0;
    for (int val : positive_values) {
        sum += val;
    }
    int average = sum / positive_values.size();
    
    // Contar valores por encima del promedio
    int above_average = 0;
    for (int val : positive_values) {
        if (val > average) {
            above_average++;
        }
    }
    
    cout << average << " " << above_average << endl;
    
    return 0;
}

/*
Entrada:
8
-5 10 3 -2 8 15 -1 6
Salida:
8 2
*/