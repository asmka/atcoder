#include <iostream>
#include <climits>
#define ANS_MAX 998244353
//#define DEBUG
using namespace std;

int countCombination(long n, long p){
    long cb = 1;

    if(p > n/2){
        p = n - p;
    }

    for(int i=n; i>n-p; i--){
        cb *= i;
    }

    for(int i=p; i>=2; i--){
        cb /= i;
    }

    return cb;
}

int main(){
    long N, A, B, K;
    long sc, ans=0;
    cin >> N >> A >> B >> K;

    // A*x + B*y + (A+B)*z = K
    // x + y + z < N;
    for(int i=0; i<=N; i++){
        for(int j=0; j<=N-i; j++){
            for(int k=0; k<=N-i-j; k++){
                sc = A*i + B*j + (A+B)*k;
#ifdef DEBUG
    cout << "sc = " << sc << ", i = " << i << ", j = " << j << ", k = " << k << endl;
#endif
                if(sc > K){
                    break;
                }else if(sc == K){
                    ans += (countCombination(N, i) *
                            countCombination(N-i, j) * 
                            countCombination(N-i-j, k));
                    if(ans > ANS_MAX){
                        ans %= ANS_MAX;
                    }
                    break;
                }
            }
        }
    }


    cout << ans << endl;
    
    return 0;
}

