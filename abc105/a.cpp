#include <iostream>
using namespace std;

int main(){
    int N, K, ans;

    cin >> N >> K;

    ans = (N % K == 0 ? 0 : 1);
    cout << ans << endl;

    return 0;
}
