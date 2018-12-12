#include<iostream>
using namespace std;

int main(){
    unsigned long long K, cnt, num;
    cin >> K;

    cnt = 0;
    num = 1;
    while(true){
        if(num < 10){
            cout << num << endl;
            cnt++;
        }else{
            if(num%10 == 9){
                cout << num << endl;
                cnt++;
            }
        }
        
        if(cnt == K){
            break;
        }
        num++;
    }
}


