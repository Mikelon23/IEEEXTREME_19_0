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