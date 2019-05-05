#include <queue>
#include <vector>
#include <string>
#include <iostream>

using namespace std;


int main() {
    int H {}, W {};
    cin >> H >> W;
    string A[H];
    for (int h=0; h<H; h++) {
        cin >> A[h];
    }

    // initialize first black positions
    queue<vector<int>*> black_list {};
    int **f = new int*[H];
    for (int h=0; h<H; h++) {
        f[h] = new int[W];
        for (int w=0; w<W; w++) {
            if (A[h][w] == '#') {
                f[h][w] = true;
                black_list.push(new vector<int> {h, w, 0});
            } else {
                f[h][w] = false;
            }
        }
    }

    int ans = 0;
    // expand black positions until all positions fill
    while (!black_list.empty()) {
        vector<int> *pos = black_list.front();
        int h = (*pos)[0];
        int w = (*pos)[1];
        int d = (*pos)[2];
        // up
        if (h-1 >= 0 && f[h-1][w] == false) {
            f[h-1][w] = true;
            black_list.push(new vector<int> {h-1, w, d+1});
        }
        // down
        if (h+1 < H && f[h+1][w] == false) {
            f[h+1][w] = true;
            black_list.push(new vector<int> {h+1, w, d+1});
        }
        // left
        if (w-1 >= 0 && f[h][w-1] == false) {
            f[h][w-1] = true;
            black_list.push(new vector<int> {h, w-1, d+1});
        }
        // right
        if (w+1 < W && f[h][w+1] == false) {
            f[h][w+1] = true;
            black_list.push(new vector<int> {h, w+1, d+1});
        }
        ans = d;
        black_list.pop();
        delete pos;
    }

    cout << ans << endl;
}
