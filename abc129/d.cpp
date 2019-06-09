#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <string>

using namespace std;

int main() {
    int H, W;
    cin >> H >> W;
    string S[H];
    for (int i=0; i<H; i++) {
        cin >> S[i];
    }

    vector<vector<vector<int>>> b;
    vector<vector<int>> bw;
    for (int w = 0; w<W; w++) {
        bw.push_back({0, 0, 0, 0});
    }
    for (int h = 0; h<H; h++) {
        b.push_back(bw);
    }

    for (int h = 0; h<H; h++) {
        for (int w = 0; w<W; w++) {
            if (S[h][w] == '#') {
                continue;
            }
            // up
            if (h-1 < 0 or S[h-1][w] == '#') {
                b[h][w][0] = 0;
            } else {
                b[h][w][0] = b[h-1][w][0] + 1;
            }
            // left
            if (w-1 < 0 or S[h][w-1] == '#') {
                b[h][w][1] = 0;
            } else {
                b[h][w][1] = b[h][w-1][1] + 1;
            }
        }
    }

    for (int h = H-1; h>=0; h--) {
        for (int w = W-1; w>=0; w--) {
            if (S[h][w] == '#') {
                continue;
            }
            // down
            if (h+1 >= H or S[h+1][w] == '#') {
                b[h][w][2] = 0;
            } else {
                b[h][w][2] = b[h+1][w][2] + 1;
            }
            // right
            if (w+1 >= W or S[h][w+1] == '#') {
                b[h][w][3] = 0;
            } else {
                b[h][w][3] = b[h][w+1][3] + 1;
            }
        }
    }

    long ans = 0;
    for (int h = 0; h<H; h++) {
        for (int w = 0; w<W; w++) {
            if (S[h][w] == '#') {
                continue;
            }
            int tmp = accumulate(b[h][w].begin(), b[h][w].end(), 0) + 1;
            if (tmp > ans) {
                ans = tmp;
            }
        }
    }
    cout << ans << endl;
    
}
