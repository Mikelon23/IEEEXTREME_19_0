#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <climits>
using namespace std;

double distancia(pair<int, int> a, pair<int, int> b) {
    return sqrt(pow(a.first - b.first, 2) + pow(a.second - b.second, 2));
}

int main() {
    int n, k;
    cin >> n >> k;
    vector<pair<int, int>> puntos(n);
    for (int i = 0; i < n; i++) {
        cin >> puntos[i].first >> puntos[i].second;
    }
    
    vector<vector<double>> dist_entre(n, vector<double>(n, 0.0));
    vector<double> dist_origen(n);
    for (int i = 0; i < n; i++) {
        dist_origen[i] = distancia({0,0}, puntos[i]);
        for (int j = 0; j < n; j++) {
            dist_entre[i][j] = distancia(puntos[i], puntos[j]);
        }
    }
    
    // DP: dp[mask][i] = distancia mínima para visitar los puntos en mask terminando en i
    vector<vector<double>> dp(1 << n, vector<double>(n, INT_MAX));
    for (int i = 0; i < n; i++) {
        dp[1 << i][i] = 2 * dist_origen[i];
    }
    
    for (int mask = 1; mask < (1 << n); mask++) {
        for (int i = 0; i < n; i++) {
            if (!(mask & (1 << i))) continue;
            for (int j = 0; j < n; j++) {
                if (mask & (1 << j)) continue;
                int new_mask = mask | (1 << j);
                double nuevo_valor = dp[mask][i] - dist_origen[i] + dist_entre[i][j] + dist_origen[j];
                if (nuevo_valor < dp[new_mask][j]) {
                    dp[new_mask][j] = nuevo_valor;
                }
            }
        }
    }
    
    double min_dist = INT_MAX;
    for (int mask = 0; mask < (1 << n); mask++) {
        if (__builtin_popcount(mask) != k) continue;
        for (int i = 0; i < n; i++) {
            if (dp[mask][i] < min_dist) min_dist = dp[mask][i];
        }
    }
    
    cout << fixed << setprecision(2) << min_dist << endl;
    return 0;
}