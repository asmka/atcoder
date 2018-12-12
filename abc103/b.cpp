#include <string>
#include <iostream>

//#define DEBUG

using namespace std;

int main(){
    string ans="No";
    string s, t;

    cin >> s >> t;

    for(int i=0; i<t.length(); i++){

#ifdef DEBUG
        cout << s << endl;
        cout << t << endl;
#endif

        if(s == t){
            ans = "Yes";
            break;
        }
        t.insert(t.begin(), t.back());
        t.pop_back();
    }

    cout << ans << endl;

    return 0;
}

