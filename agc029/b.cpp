#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main() {
    unsigned int N;
    cin >> N;

    vector<unsigned int> A(N);
    for (int i=0; i<N; i++) {
        unsigned int a;
        cin >> a;
        A[i] = a;
    }
    sort(A.begin(), A.end());
    
    unsigned int prev = 0;
    vector<unsigned int> compA {};
    map<unsigned int, int> cntA {};
    for (int i=0; i<N; i++) {
        if (prev != A[i]) {
            compA.push_back(A[i]);
            cntA.insert(make_pair(A[i], 1));
            prev = A[i];
        } else {
            cntA[A[i]]++;
        }
    }

    int ans = 0;
    int hbit = 31;
    for (int i = compA.size()-1; i >= 0; i--) {
        unsigned int a = compA[i];
        //cout << a << endl;
        while ((a & (1 << hbit)) == 0) {
            hbit--;
        }

        unsigned int p = ((~a << (31-hbit)) >> (31-hbit)) + 1;
        //cout << "a: " << a << endl;
        //cout << "p: " << p << endl;
        if (a == p) {
            ans += cntA[a]/2;
        } else {
            int anum = cntA[a];
            int pnum = 0;
            if (binary_search(compA.begin(), compA.end(), p)) {
                pnum = cntA[p];
            }
            if (anum < pnum) {
                ans += anum;
                cntA[p] -= anum;
            } else {
                ans += pnum;
                cntA[p] -= pnum;
            }
        }
    }

    cout << ans << endl;

    return 0;
}
