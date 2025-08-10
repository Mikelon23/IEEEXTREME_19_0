#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    if (!(cin >> s)) return 0;
    int n = (int)s.size();

    // next_table has (n+1) rows and 26 columns stored flat:
    // next_table[i*26 + c] = first index >= i where s[index] == c+'a', or -1
    vector<int> next_table((n + 1) * 26, -1);

    // initialize last row (position n) to -1 (already done by vector init)
    for (int i = n - 1; i >= 0; --i) {
        // copy from i+1
        int base_i = i * 26;
        int base_ip1 = (i + 1) * 26;
        for (int c = 0; c < 26; ++c) next_table[base_i + c] = next_table[base_ip1 + c];
        // set current character
        next_table[base_i + (s[i] - 'a')] = i;
    }

    int q;
    cin >> q;
    while (q--) {
        string p;
        cin >> p;
        int m = (int)p.size();

        auto can = [&](int k) -> bool {
            // check whether suffix of length k (p[m-k .. m-1]) is a subsequence of s
            int pos = 0; // current search position in s (0..n)
            int start = m - k;
            for (int i = start; i < m; ++i) {
                int c = p[i] - 'a';
                int nxt = next_table[pos * 26 + c];
                if (nxt == -1) return false;
                pos = nxt + 1;
                if (pos > n && i < m-1) return false; // no more chars in s
            }
            return true;
        };

        // binary search maximum k in [0..m]
        int lo = 0, hi = m;
        while (lo < hi) {
            int mid = (lo + hi + 1) >> 1;
            if (can(mid)) lo = mid;
            else hi = mid - 1;
        }
        cout << lo << '\n';
    }

    return 0;
}
