#include <string>
#include <iostream>
using namespace std;

int main() {
    long N;
    string S;
    long Q;
    cin >> N;
    cin >> S;
    cin >> Q;
    long kA[Q];
    for(long i=0; i<Q; i++){
        cin >> kA[i];
    }

    for (long q=0; q<Q; q++) {
        long k = kA[q];
        long Dcnt = 0;
        long Mcnt = 0;
        long DMcnt = 0;
        long DMCcnt = 0;
        for (long i=0; i<S.length(); i++) {
            if (i-k >= 0 && S[i-k] == 'D') {
                Dcnt--;
                DMcnt -= Mcnt;
            } else if (i-k >= 0 && S[i-k] == 'M') {
                Mcnt--;
            }

            if (S[i] == 'D') {
                Dcnt++;
            } else if (S[i] == 'M') {
                Mcnt++;
                DMcnt += Dcnt;
            } else if (S[i] == 'C') {
                DMCcnt += DMcnt;
            }
        }
        cout << DMCcnt << endl;
    }
}
    
