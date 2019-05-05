#include <string>
#include <iostream>

using namespace std;


int main() {
    int H, W, N;
    int sr, sc;
    string S;
    string T;

    cin >> H >> W >> N;
    cin >> sr >> sc;
    cin >> S;
    cin >> T;

    string ans = "YES";

    // up down
    int f_h = 0;
    int l_h = H-1;
    for (int i=N-1; i>=0; i--) {
        if (T[i] == 'U') {
            l_h = min(l_h+1, H-1);
        } else if (T[i] == 'D') {
            f_h = max(f_h-1, 0);
        }
        if (S[i] == 'U') {
            f_h = f_h+1;
        } else if (S[i] == 'D') {
            l_h = l_h-1;
        }
        if (f_h > l_h) {
            ans = "NO";
        }
    }

    // left right
    int f_w = 0;
    int l_w = W-1;
    for (int i=N-1; i>=0; i--) {
        if (T[i] == 'L') {
            l_w = min(l_w+1, W-1);
        } else if (T[i] == 'R') {
            f_w = max(f_w-1, 0);
        }
        if (S[i] == 'L') {
            f_w = f_w+1;
        } else if (S[i] == 'R') {
            l_w = l_w-1;
        }
        if (f_w > l_w) {
            ans = "NO";
        }
    }

    if (sr-1 < f_h or l_h < sr-1 or sc-1 < f_w or l_w < sc-1) {
        ans = "NO";
    }

    //cout << f_h << l_h << f_w << l_w << endl;
    cout << ans << endl;
}

