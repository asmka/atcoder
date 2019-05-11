#include <vector>
#include <string>
#include <iostream>

using namespace std;


int countAB(string str) {
    int cnt = 0;
    for (int i=0; i<str.length()-1; i++) {
        if (str[i] == 'A' and str[i+1] == 'B') {
            cnt += 1;
        }
    }
    return cnt;
}


int main() {
    int N;
    cin >> N;
    string s[N];
    vector<string> BstrA {}, BstrX {}, XstrA {}, XstrX {};
    for (int i=0; i<N; i++) {
        cin >> s[i];
        if (s[i].front() == 'B' and s[i].back() == 'A') {
            //cout << "DEBUG BstrA push" << endl;
            BstrA.push_back(s[i]);
        } else if (s[i].front() == 'B') {
            //cout << "DEBUG BstrX push" << endl;
            BstrX.push_back(s[i]);
        } else if (s[i].back() == 'A') {
            //cout << "DEBUG XstrA push" << endl;
            XstrA.push_back(s[i]);
        } else {
            //cout << "DEBUG XstrX push" << endl;
            XstrX.push_back(s[i]);
        }
    }

    //cout << "DEBUG" << endl;
    // top string
    string cur_str {};
    if (XstrA.size() > 0) {
        cur_str = XstrA.back();
        XstrA.pop_back();
    } else if (BstrA.size() > 0) {
        cur_str = BstrA.back();
        BstrA.pop_back();
    } else if (BstrX.size() > 0) {
        cur_str = BstrX.back();
        BstrX.pop_back();
    } else {
        cur_str = XstrX.back();
        XstrX.pop_back();
    }

    //cout << "DEBUG" << endl;
    int ans = 0;
    bool Aflag = false;
    ans += countAB(cur_str);
    if (cur_str.back() == 'A') {
        Aflag = true;
    }

    //cout << "DEBUG" << endl;
    for (int i=0; i<BstrA.size(); i++) {
        cur_str = BstrA[i];
        if (Aflag) {
            ans += 1;
        }
        ans += countAB(cur_str);
        Aflag = true;
    }

    //cout << "DEBUG" << endl;
    int bxi = 0;
    int xai = 0;
    while (true) {
        if (not (bxi < BstrX.size()) and not (xai < XstrA.size())) {
            break;
        }

        if (bxi < BstrX.size()) {
            cur_str = BstrX[bxi];
            if (Aflag) {
                ans += 1;
            }
            ans += countAB(cur_str);
            Aflag = false;
            bxi += 1;
        }

        if (xai < XstrA.size()) {
            cur_str = XstrA[xai];
            ans += countAB(cur_str);
            Aflag = true;
            xai += 1;
        }
    }

    //cout << "DEBUG" << endl;
    for (int i=0; i<XstrX.size(); i++) {
        cur_str = XstrX[i];
        ans += countAB(cur_str);
    }

    cout << ans << endl;
}


