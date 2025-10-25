#include <iostream>
#include <vector>
using namespace std;

// Find first occurrence of x
int findFirst(const vector<int>& arr, int x) {
    int left = 0, right = arr.size() - 1;
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == x) {
            result = mid;
            right = mid - 1; // Continue searching in left half
        } else if (arr[mid] < x) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return result;
}

// Find last occurrence of x
int findLast(const vector<int>& arr, int x) {
    int left = 0, right = arr.size() - 1;
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == x) {
            result = mid;
            left = mid + 1; // Continue searching in right half
        } else if (arr[mid] < x) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, q;
    cin >> n >> q;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    for (int i = 0; i < q; i++) {
        int x;
        cin >> x;
        
        int first = findFirst(arr, x);
        int last = findLast(arr, x);
        
        if (first == -1) {
            cout << "-1 -1\n";
        } else {
            cout << first + 1 << " " << last + 1 << "\n";
        }
    }
    
    return 0;
}