#include <vector>
#include <map>
#include <algorithm>
#include <iostream>

//#define DEBUG

using namespace std;

int main(){
    int N, M;
    int ans=0;

    cin >> N >> M;

    vector<pair<int, int> > pairs(M);
    for(int i=0; i<M; i++){
#ifdef DEBUG
        cout << "M = " << M << ", i=" << i << endl;
#endif
        int ta, tb;
        cin >> ta >> tb;
        pairs[i] = make_pair(ta, tb);
    }

    sort(pairs.begin(), pairs.end());

    int prev_f = -1;
    int tmax = -1;
    for(int i=0; i<M; i++){

        // 同じ始動の橋なのでスルー
        if(pairs[i].first == prev_f){
            continue;
        }

        // 新規橋はいらない
        if(pairs[i].first <= tmax){
            // 橋を左に移動
            if(pairs[i].second - 1 < tmax){
                tmax = pairs[i].second - 1;
            }
        // 新規橋を作成
        }else{
            tmax = pairs[i].second - 1;
            ans++;
        }
    }

    cout << ans << endl;

    return 0;
}
