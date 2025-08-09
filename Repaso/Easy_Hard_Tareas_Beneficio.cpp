// 3. Nivel Difícil — Programación de Tareas con Beneficio (Weighted Interval Scheduling)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct Task {
    ll start, end, profit;
    bool operator<(Task const& t) const {
        return end < t.end;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<Task> T(N);
    for (int i = 0; i < N; i++) {
        cin >> T[i].start >> T[i].end >> T[i].profit;
    }
    sort(T.begin(), T.end());  // ordenamos por tiempo de fin

    // Preparamos un array de tiempos de fin para bin-search
    vector<ll> ends(N);
    for (int i = 0; i < N; i++) ends[i] = T[i].end;

    // dp[i] = máximo beneficio usando tareas [0..i-1]
    vector<ll> dp(N+1, 0);
    for (int i = 1; i <= N; i++) {
        // beneficio sin tomar la i-ésima
        ll no_tomar = dp[i-1];
        // beneficio tomando la i-ésima
        // buscamos la última tarea que termine ≤ start_i
        ll profit_i = T[i-1].profit;
        ll s = T[i-1].start;
        int j = int(upper_bound(ends.begin(), ends.end(), s) - ends.begin());
        // j es el número de tareas cuyo end ≤ s, por tanto usamos dp[j]
        ll tomar = profit_i + dp[j];
        dp[i] = max(no_tomar, tomar);
    }

    cout << dp[N] << "\n";
    return 0;
}

/*Entrada:
4
1 3 50
3 5 20
6 19 100
2 100 200
Salida:
250
*/