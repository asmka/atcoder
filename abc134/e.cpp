#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {
    long N;
    cin >> N;

    multiset<long> s {};
    for (long i=0; i<N; i++) {
        long a;
        cin >> a;

        // cout << "i: " << i << endl;
        // cout << "a: " << a << endl;
        // cout << "s.begin(): " << *(s.begin()) << endl;
        // cout << "s.end(): " << *(s.end()) << endl;
        if (i == 0) {
            s.insert(a);
        } else {
            auto itr = s.lower_bound(a);
            //cout << "a: " << a <<  ", lower_bound: " << *itr << endl;
            if (itr == s.begin()) {
                //cout << "insert: " << a << endl;
                s.insert(a);
            } else {
                //cout << "update: " << *(--itr) << " -> " << a << endl;
                s.erase(--itr);
                s.insert(a);
            }
        }
    }
    
    cout << s.size() << endl;
    // cout << "s.begin(): " << *(s.begin()) << endl;
    // cout << "s.end(): " << *(s.end()) << endl;
    //for (auto itr=s.begin(); itr!=s.end(); itr++) {
    //    cout << "s: " << *itr << endl;
    //}
}
