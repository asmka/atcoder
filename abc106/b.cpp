#include <iostream>
using namespace std;

int main() {
    int N;
    int cnt = 0, ans = 0;

    cin >> N;

    for (int n = 1; n <= N; n+=2) {
        cnt = 0;

        for (int v = 1; v <= n; v++) {
            // can divide
            if (n % v == 0) {
                cnt++;
            }
        }
        if (cnt == 8) {
            ans++;
        }
    }

    cout << ans << endl;

    return 0;
}
