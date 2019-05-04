#include <map>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

int H, W;


void fillUp(int **d, int h, int w, int cur_distance) {
    int ch = h - 1;
    int cd = cur_distance + 1;
    while (ch >= 0 && cd < d[ch][w]) {
        d[ch][w] = cd;
        ch -= 1;
        cd += 1;
    }
}


void fillDown(int **d, int h, int w, int cur_distance) {
    int ch = h + 1;
    int cd = cur_distance + 1;
    while (ch < H && cd < d[ch][w]) {
        d[ch][w] = cd;
        ch += 1;
        cd += 1;
    }
}

void debug(int **d) {
    //cout << "H: " << H << endl;
    //cout << "W: " << W << endl;
    for (int h=0; h<H; h++) {
        for (int w=0; w<W; w++) {
            cout << d[h][w] << ' ';
        }
        cout << endl;
    }
}

void fillDistance(int** d, int h, int w) {
    int cw, cd;

    // updown
    fillUp(d, h, w, 0);
    fillDown(d, h, w, 0);
    //debug(d);

    // left
    cw = w - 1;
    cd = 1;
    while (cw >= 0 && cd < d[h][cw]) {
        d[h][cw] = cd;
        fillUp(d, h, cw, cd);
        fillDown(d, h, cw, cd);
        cw -= 1;
        cd += 1;
    }

    // right
    cw = w + 1;
    cd = 1;
    while (cw < W && cd < d[h][cw]) {
        d[h][cw] = cd;
        fillUp(d, h, cw, cd);
        fillDown(d, h, cw, cd);
        cw += 1;
        cd += 1;
    }
}


int main() {
    cin >> H >> W;
    string A[H];
    for (int h=0; h<H; h++) {
        cin >> A[h];
    }
    int **d = new int*[H];
    for (int h=0; h<H; h++) {
        d[h] = new int[W];
        for (int w=0; w<W; w++) {
            if (A[h][w] == '#') {
                d[h][w] = 0;
            } else {
                d[h][w] = 10000;
            }
            //cout << d[h][w];
        }
    }

    for (int h=0; h<H; h++) {
        for (int w=0; w<W; w++) {
            if (A[h][w] == '#') {
                fillDistance(d, h, w);
            }
        }
    }

    int ans = -1;
    for (int h=0; h<H; h++) {
        for (int w=0; w<W; w++) {
            //cout << d[h][w];
            if (d[h][w] > ans) {
                ans = d[h][w];
            }
        }
    }
    //debug(d);

    cout << ans << endl;
}
