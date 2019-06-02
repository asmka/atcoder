#include <iostream>
#include <string>
using namespace std;

// AAABC
// AABCA
// ABCAA
// BCAAA
int main() {
    string s {};
    cin >> s;

    long cnt = 0;
    if (s.length() >= 3) {
        int Acnt = 0;
        for (int i=0; i<s.length()-2; i++) {
            if (s[i] == 'A') {
                Acnt += 1;
            } else {
                Acnt = 0;
            }
            if (s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'C') {
                s[i] = 'B';
                s[i+1] = 'C';
                s[i+2] = 'A';
                cnt += Acnt;
                if (Acnt >= 2) {
                    s[i+1] = 'A';
                }

                if (Acnt >= 3) {
                    Acnt -= 2;
                } else {
                    Acnt = 0;
                }
            }
        }
    }
    cout << cnt << endl;
}

