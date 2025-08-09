// 2. Nivel Intermedio — Máximo Área de Triángulo (Rotating Calipers sobre el Convex Hull)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Point {
    ll x, y;
    bool operator<(Point const& p) const {
        return x < p.x || (x == p.x && y < p.y);
    }
};

// Producto cruzado (B - A) × (C - A)
ll cross(const Point& A, const Point& B, const Point& C) {
    return (B.x - A.x) * (C.y - A.y)
         - (B.y - A.y) * (C.x - A.x);
}

// Construye el convex hull en O(N log N)
vector<Point> convexHull(vector<Point>& pts) {
    int n = pts.size(), k = 0;
    if (n <= 1) return pts;
    sort(pts.begin(), pts.end());
    vector<Point> H(2*n);
    // Parte inferior
    for (int i = 0; i < n; ++i) {
        while (k >= 2 && cross(H[k-2], H[k-1], pts[i]) <= 0) k--;
        H[k++] = pts[i];
    }
    // Parte superior
    for (int i = n-2, t = k+1; i >= 0; --i) {
        while (k >= t && cross(H[k-2], H[k-1], pts[i]) <= 0) k--;
        H[k++] = pts[i];
    }
    H.resize(k-1);
    return H;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<Point> pts(N);
    for (int i = 0; i < N; i++) {
        cin >> pts[i].x >> pts[i].y;
    }
    auto H = convexHull(pts);
    int M = H.size();
    if (M < 3) {
        cout << fixed << setprecision(6) << 0.0 << "\n";
        return 0;
    }

    // Rotating calipers para máximo área de triángulo en polígono convexo
    ll best2A = 0;  // guardamos el doble de área
    for (int i = 0; i < M; i++) {
        int k = (i + 2) % M;
        for (int j = (i+1)%M; j != i; j = (j+1)%M) {
            // avanzamos k mientras aumente el área
            while (true) {
                int nk = (k + 1) % M;
                ll curr = abs(cross(H[i], H[j], H[k]));
                ll next = abs(cross(H[i], H[j], H[nk]));
                if (next > curr) k = nk;
                else break;
            }
            best2A = max(best2A, abs(cross(H[i], H[j], H[k])));
            if ((j+1)%M == (i)) break;
        }
    }

    double area = best2A / 2.0;
    cout << fixed << setprecision(6) << area << "\n";
    return 0;
}

/*
Entrada:
4
0 0
5 0
0 5
2 2
Salida:
12.500000
*/