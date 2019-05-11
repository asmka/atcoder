#include <cmath>
#include <string>
#include <iostream>

using namespace std;

int main() {
    long N;
    cin >> N;

    long ans = 0;

    long dmax = long(sqrt(N))+1;
    //cout << "DEBUG dmax: " << dmax << endl;
    for (long d=1; d<=dmax; d++) {
        if (N % d != 0) {
            continue;
        }
        long m = N/d - 1;
        if (m>0 and N%m == N/m) {
            ans += m;
        }
    }

    cout << ans << endl;
}


