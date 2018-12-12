#include <string>
#include <iostream>
using namespace std;
//constexpr long long kFiveTrillion = 500000000000;

int main() {
    string S;
    int K;
    long long cnt=0;
    char ans = '0';

    cin >> S >> K;

    for (int i = 0; i < S.length(); i++) {
        if (i + 1 == K) {
            ans = S[i];
            break;
        } else if (S[i] != '1') {
            ans = S[i];
            break;
        }
    }

    cout << ans << endl;

    return 0;
}
