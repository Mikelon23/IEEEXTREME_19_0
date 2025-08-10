#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        int c, n;
        cin >> c >> n;
        vector<int> dp(c + 1, 0);

        for (int i = 0; i < n; ++i) {
            int w, f;
            cin >> w >> f;
            if (w > c) {
                // item too heavy for any capacity, skip updates
                continue;
            }
            // iterate backwards to enforce 0/1 (each item used at most once)
            for (int cap = c; cap >= w; --cap) {
                dp[cap] = max(dp[cap], dp[cap - w] + f);
            }
        }

        cout << dp[c] << '\n';
    }

    return 0;
}
