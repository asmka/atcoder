#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;

int main() {
    long N, Q;
    cin >> N >> Q;
    //priority_queue<vector<long>, vector<vector<long>>, greater<vector<long>>> tl;
    vector<vector<long>> tl {};
    for (int i=0; i<N; i++) {
        long S, T, X;
        cin >> S >> T >> X;
        tl.push_back({T-X, 0, X});
        tl.push_back({S-X, 1, X});
    }
    for (int i=0; i<Q; i++) {
        long D;
        cin >> D;
        tl.push_back({D, 2, 0});
    }
    sort(tl.begin(), tl.end());

    vector<long> ans {};
    multiset<long> Xset {};
    for (auto itl=tl.begin(); itl!=tl.end(); itl++) {
        long mode = (*itl)[1];
        long X = (*itl)[2];
        //cout << t[0] << ' ' << mode << ' ' << X << endl;
        if (mode == 0) {
            // T
            Xset.erase(X);
        } else if (mode == 1) {
            // S
            Xset.insert(X);
        } else {
            // D
            if (not Xset.empty()) {
                auto it = Xset.begin();
                ans.push_back(*it);
            } else {
                ans.push_back(-1);
            }
        }
    }

    for (auto it=ans.begin(); it!=ans.end(); it++) {
        cout << *it << endl;
    }
}
