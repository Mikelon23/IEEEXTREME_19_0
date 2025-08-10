#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// functions used to comunicate with the interactor (the other program)
// use this to get the position of the other player.
// after using it you must do your own move
// TL;DR GetBlack() GetBlack() is invalid
int GetBlack() {
    int black_king_node;
    cin >> black_king_node;
    return black_king_node;
}

// use this to set your own move
void SetWhite(int node) {
    cout << node << endl;
}

int n, m;

void ReadGraph() {
    cin >> n >> m;
    for (int i = 0; i < m; i += 1) {
        int a, b;
        cin >> a >> b;
    }
}

int main() {
    // use this to pass the first example
    ReadGraph();
    SetWhite(2);
    GetBlack();
    SetWhite(6);
    GetBlack();
    SetWhite(3);
    return 0;
}

