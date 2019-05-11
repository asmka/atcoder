#include <string>
#include <iostream>

using namespace std;

int main() {
    int R, G, B, N;
    cin >> R >> G >> B >> N;

    int ans = 0;
    for (int r=0; r<3001; r++) {
        int balls = R*r;
        if (N < balls) {
            break;
        }
        for (int g=0; g<3001; g++) {
            balls = R*r + G*g;
            if (N < balls) {
                break;
            }
            int left = N - balls;
            if (left%B == 0) {
                ans += 1;
            }
        }
    }

    cout << ans << endl;
}

