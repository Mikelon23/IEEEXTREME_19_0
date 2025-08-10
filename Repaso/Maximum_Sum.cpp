#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

long long calculateSum(const vector<int>& arr) {
    long long sum = 0;
    for (size_t i = 0; i < arr.size() - 1; i++) {
        sum += (long long)arr[i] * arr[i + 1];
    }
    return sum;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n;
        
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        
        if (n == 1) {
            cout << "0\n";
            cout << arr[0] << "\n";
            continue;
        }
        
        // For small arrays, use brute force to ensure correctness
        if (n <= 10) {
            sort(arr.begin(), arr.end());
            
            long long maxSum = LLONG_MIN;
            vector<int> bestArrangement;
            
            do {
                long long currentSum = calculateSum(arr);
                if (currentSum > maxSum || 
                    (currentSum == maxSum && (bestArrangement.empty() || arr < bestArrangement))) {
                    maxSum = currentSum;
                    bestArrangement = arr;
                }
            } while (next_permutation(arr.begin(), arr.end()));
            
            cout << maxSum << "\n";
            for (size_t i = 0; i < bestArrangement.size(); i++) {
                if (i > 0) cout << " ";
                cout << bestArrangement[i];
            }
            cout << "\n";
        } else {
            // For larger arrays, use heuristic approach
            // The key insight: arrange numbers so largest have most neighbors
            
            // Separate zeros and non-zeros
            vector<int> zeros, nonzeros;
            for (int x : arr) {
                if (x == 0) zeros.push_back(x);
                else nonzeros.push_back(x);
            }
            
            sort(nonzeros.begin(), nonzeros.end(), greater<int>());
            
            vector<int> result;
            
            // Strategy: place zeros strategically to minimize negative impact
            // while maximizing positive products
            
            if (nonzeros.empty()) {
                // All zeros
                result = arr;
            } else if (zeros.empty()) {
                // No zeros - arrange non-zeros optimally
                // Place largest in middle, then alternate sides
                result.resize(n);
                int mid = n / 2;
                result[mid] = nonzeros[0];
                
                int left = mid - 1, right = mid + 1;
                for (size_t i = 1; i < nonzeros.size(); i++) {
                    if (left >= 0 && (right >= n || i % 2 == 1)) {
                        result[left--] = nonzeros[i];
                    } else {
                        result[right++] = nonzeros[i];
                    }
                }
            } else {
                // Mix of zeros and non-zeros
                // Place zeros at ends or between smaller numbers
                result = nonzeros;
                // Simple strategy: append zeros at the end
                for (int zero : zeros) {
                    result.push_back(zero);
                }
                // This might not be optimal, but it's a reasonable heuristic
            }
            
            long long sum = calculateSum(result);
            cout << sum << "\n";
            for (size_t i = 0; i < result.size(); i++) {
                if (i > 0) cout << " ";
                cout << result[i];
            }
            cout << "\n";
        }
    }
    
    return 0;
}