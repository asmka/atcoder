#include <algorithm>
#include <string>
#include <iostream>

#define DEBUG

using namespace std;


string RtnRvsBinExp(int num) {
    string bin = "";

    if(num <= 0){
        cout << "ERROR: invalid function argument (line: "
            << __LINE__ << ")" << endl;
        exit(1);
    }

    while(num > 0){
        if(num % 2 == 0){
            bin += "0";
        }else{
            bin += "1";
        }
        num /= 2;
    }

    return bin;
}


void AddBit(char &bit) {
    if(bit == '0'){
        bit = '1';
    }else if(bit == '1'){
        bit = '2';
    }else{
        cout << "ERROR: invalid function argument (line: "
            << __LINE__ << ")" << endl;
        exit(1);
    }
}


void FormRvsBin(string &bin) {
    int i=0;
    while(i < bin.length()){
        if(bin[i] == '2'){
            if(!(i+1 < bin.length())){
                bin += "1";
            }else{
                AddBit(bin[i+1]);
            }
            bin[i] = '0';
        }
        i++;
    }
}


void ConvRvsBinMns(string &bin, bool negative) {
    int i=0;

    while(i < bin.length()){
        if( (!negative && i%2 == 1 || negative && i%2 == 0) && bin[i] == '1'){
            if(!(i+1 < bin.length())){
                bin += "1";
            }else{
                AddBit(bin[i+1]);
            }
            FormRvsBin(bin);
        }
        i++;
    }
}


int main(){
    int N;
    bool negative;
    string ans;

    cin >> N;
    if(N < 0){
        negative = true;
        N *= -1;
    }else{
        negative = false;
    }

    if(N == 0){
        ans = "0";
    }else{
        ans = RtnRvsBinExp(N);
        ConvRvsBinMns(ans, negative);
        reverse(ans.begin(), ans.end());
    }

    cout << ans << endl;

    return 0;
}

