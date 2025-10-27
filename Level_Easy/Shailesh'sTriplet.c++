#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    
    while (t--) {
        long long n;
        cin >> n;
        if (n % 2 == 1) {
            cout << "-1\n";
            continue;
        }
        bool found = false;
        long long a, b, c;
        set<long long> candidates;
        candidates.insert(1);
        candidates.insert(2);
        
        long long half = n / 2;
        for (int delta = -10; delta <= 10; delta++) {
            if (half + delta > 0) candidates.insert(half + delta);
        }
        
        for (int delta = -10; delta <= 10; delta++) {
            if (n + delta > 0) candidates.insert(n + delta);
        }
        
        candidates.insert(2 * n - 1);
        candidates.insert(2 * n - 2);
        for (long long a_val : candidates) {
            if (found) break;
            for (long long b_val : candidates) {
                if (found || a_val == b_val) continue;
                
                c = 2 * n - a_val - b_val;
                
                if (c > 0 && c != a_val && c != b_val && (a_val ^ b_val ^ c) == n) {
                    a = a_val;
                    b = b_val;
                    found = true;
                    break;
                }
            }
        }
        
        if (found) {
            cout << a << " " << b << " " << c << "\n";
        } else {
            cout << "-1\n";
        }
    }
    
    return 0;
}