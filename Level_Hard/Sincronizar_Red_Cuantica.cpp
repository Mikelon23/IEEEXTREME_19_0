/* Ejercicio de Nivel Difícil: Sincronización de Red Cuántica
Descripción del Problema
Una red cuántica consta de n nodos, cada uno con un estado binario (0 o 1). Cada segundo, los nodos actualizan su estado simultáneamente según la siguiente regla:

Si un nodo tiene al menos 2 vecinos con estado 1, cambia su estado (0 se convierte en 1, o 1 se convierte en 0).

Los nodos marcados como magnetizados no cambian su estado nunca.

El objetivo es determinar cuántos segundos tardará la red en alcanzar un estado estable (donde ningún nodo cambia). Si la red entra en un ciclo infinito, se debe retornar -1.

Entrada
La primera línea contiene n (número de nodos) y m (número de aristas).

Las siguientes m líneas contienen dos enteros u y v que representan una arista no dirigida entre los nodos u y v.

La siguiente línea es una cadena de longitud n que representa el estado inicial de los nodos (cadena binaria).

La última línea comienza con un entero k (número de nodos magnetizados), seguido de k enteros que son los índices de los nodos magnetizados.

Salida
Un entero que representa el número de segundos hasta alcanzar un estado estable, o -1 si se detecta un ciclo infinito. */
#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    
    string estado_str;
    cin >> estado_str;
    vector<int> estado(n);
    for (int i = 0; i < n; i++) {
        estado[i] = estado_str[i] - '0';
    }
    
    int k;
    cin >> k;
    set<int> magnetizados;
    for (int i = 0; i < k; i++) {
        int node;
        cin >> node;
        magnetizados.insert(node);
    }
    
    map<vector<int>, int> visited;
    int steps = 0;
    
    while (visited.find(estado) == visited.end()) {
        visited[estado] = steps;
        vector<int> next_estado = estado;
        bool changed = false;
        
        for (int nodo = 0; nodo < n; nodo++) {
            if (magnetizados.find(nodo) != magnetizados.end()) continue;
            
            int count_1 = 0;
            for (int vecino : graph[nodo]) {
                if (estado[vecino] == 1) count_1++;
            }
            
            if (count_1 >= 2) {
                next_estado[nodo] = 1 - estado[nodo];
                changed = true;
            }
        }
        
        if (!changed) {
            cout << steps << endl;
            return 0;
        }
        
        estado = next_estado;
        steps++;
    }
    
    cout << -1 << endl;
    return 0;
}