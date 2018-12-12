#include <iostream>
#include <string>
using namespace std;
constexpr int kMaxCityNum = 500;

int main() {
    int N, M, Q;
    int L, R;
    int p, q;
    int ans = 0;
    int l_bit[kMaxCityNum/10] = {0};
    int r_bit[kMaxCityNum/10] = {0};

    cin >> N >> M >> Q;

    for (int i = 0; i < M; i++) {
        cin >> L >> R;
        L << (i%10);
        R << (i%10);
        l_bit[M/10] |= (1 << (M%10));
        r_bit[M/10] |= (1 << (M%10));
    }

    for (int i = 0; i < Q; i++) {
        cin >> p >> q;
        ans=0;
        for (int j = 0; j < q - 1; j++) {
            
        }
        cout << ans << endl;
    }

    return 0;
}
