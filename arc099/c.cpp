#include<iostream>
using namespace std;

int main(){
    int N, K, ans;
    cin >> N >> K;
    ans = 1 + ((N - K) + ((K - 1) - 1)) / (K - 1);
    printf("%d\n", ans);
}

