#include <string>
#include <iostream>
using namespace std;

int main(){
    int N;
    int cake_val = 4;
    int donut_val = 7;
    string ans = "No";

    cin >> N;

    int i=0;
    while( (N - cake_val * i) >= 0 ){
        if( (N - cake_val * i) % donut_val == 0) {
            ans = "Yes";
            break;
        }
        i++;
    }

    cout << ans << endl;

    return 0;
}

