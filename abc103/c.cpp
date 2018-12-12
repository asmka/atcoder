#include <string>
#include <iostream>

//#define DEBUG

using namespace std;

int main(){
    int N, tmpa;
    int ans=0;

    cin >> N;

    for(int i=0; i<N; i++){
        cin >> tmpa;
        ans += tmpa - 1;
    }

    cout << ans << endl;

    return 0;
}
