#include <vector>
#include <iostream>

using namespace std;

int MaxDistance(int a, int b, int c){
    int md=0;
    int td1, td2, td3;

    td1=a-b;
    td2=a-c;
    td3=b-c;

    if(td1<0)td1*=-1;
    if(td2<0)td2*=-1;
    if(td3<0)td3*=-1;

    md = td1;
    if(md < td2){
        md = td2;
    }
    if(md < td3){
        md = td3;
    }

    return md;
}

int main(){
    int A1, A2, A3;

    cin >> A1 >> A2 >> A3;

    cout << MaxDistance(A1, A2, A3) << endl;

    return 0;
}
