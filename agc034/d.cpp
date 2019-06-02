#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<vector<long>> rpos {};
    vector<vector<long>> bpos {};
    map<string, int> rnum {};
    map<string, int> bnum {};

    for (int i=0; i<N; i++) {
        long rx, ry, rc;
        cin >> rx >> ry >> rc;
        string key = to_string(rx) + '_' + to_string(ry);
        //cout << "rkey: " << key << endl;
        auto itr = rnum.find(key);
        if (itr == rnum.end()) {
            rnum[key] = rc;
            rpos.push_back(vector<long> {rx, ry});
        } else {
            rnum[key] += rc;
        }
    }
    for (int i=0; i<N; i++) {
        long bx, by, bc;
        cin >> bx >> by >> bc;
        string key = to_string(bx) + '_' + to_string(by);
        //cout << "bkey: " << key << endl;
        auto itr = bnum.find(key);
        if (itr == bnum.end()) {
            bnum[key] = bc;
            bpos.push_back(vector<long> {bx, by});
        } else {
            bnum[key] += bc;
        }
    }

    vector<vector<long>> dis {};
    for (auto ritr=rpos.begin(); ritr!=rpos.end(); ritr++) {
        for (auto bitr=bpos.begin(); bitr!=bpos.end(); bitr++) {
            long d = abs((*ritr)[0] - (*bitr)[0]) + abs((*ritr)[1] - (*bitr)[1]);
            dis.push_back(vector<long> {d, (*ritr)[0], (*ritr)[1], (*bitr)[0], (*bitr)[1]});
        }
    }
    sort(dis.rbegin(), dis.rend());

    long ans = 0;
    for (auto itr=dis.begin(); itr!=dis.end(); itr++) {
        long d = (*itr)[0];
        long rx = (*itr)[1];
        long ry = (*itr)[2];
        long bx = (*itr)[3];
        long by = (*itr)[4];
        //cout << d << rx << ry << bx << by << endl;

        string rkey = to_string(rx) + '_' + to_string(ry);
        string bkey = to_string(bx) + '_' + to_string(by);
        //cout << "rkey: " << rkey << endl;
        //cout << "bkey: " << bkey << endl;
        auto ritr = rnum.find(rkey);
        auto bitr = bnum.find(bkey);
        if (ritr == rnum.end() or bitr == bnum.end()) {
            continue;
        } else {
            int rcnt = ritr->second;
            int bcnt = bitr->second;
            int pcnt = min(rcnt, bcnt);
            cout << d << rcnt << bcnt << pcnt << endl;
            ans += d*pcnt;
            if (rcnt == pcnt) {
                rnum.erase(ritr);
            } else {
                ritr->second -= pcnt;
            }
            if (bcnt == pcnt) {
                bnum.erase(bitr);
            } else {
                bitr->second -= pcnt;
            }
        }
    }
    cout << ans << endl;
}

