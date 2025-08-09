// 1. Nivel Fácil — Pares con Suma Objetivo
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    ll K;
    cin >> N >> K;
    vector<ll> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    unordered_map<ll, ll> cnt;
    ll pares = 0;
    for (ll x : A) {
        // Cada vez que vemos x, contamos cuántos K-x ya habíamos visto
        pares += cnt[K - x];
        // Luego añadimos x al mapa
        cnt[x]++;
    }

    cout << pares << "\n";
    return 0;
}

/*
Entrada:
5 7
1 6 3 4 5
Salida:
2
*/