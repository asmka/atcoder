#include <iostream>
#include <climits>
using namespace std;

int sumDigit(int a, int b){
    int sd=0;
    while (a > 0) {
        sd += a % 10;
        a /= 10;
    }
    while (b > 0) {
        sd += b % 10;
        b /= 10;
    }

    return sd;
}

int main(){
    int N, min=INT_MAX;

    cin >> N;
    for(int i=1; i<N; i++){
        int j = N - i;
        int sd;
        
        sd = sumDigit(i, j);
        if(sd < min) min = sd;
    }
    
    cout << min << endl;

    return 0;
}
