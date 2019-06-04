#include <iostream>
#include <climits>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main() {
    long N, X;
    cin >> N >> X;
    vector<vector<long>> maxLead {};
    long border = 0;
    for (int i=0; i<N; i++) {
        long b, l, u;
        cin >> b >> l >> u;
        long s = b * l + (X - b) * u;
        maxLead.push_back(vector<long> {s, b, l, u});
        border += b * l;
    }
    sort(maxLead.rbegin(), maxLead.rend());

    vector<long> sumMaxLead {};
    { 
        long prevSum=0;
        for (int i=0; i<N; i++) {
            long curSum = prevSum + maxLead[i][0];
            sumMaxLead.push_back(curSum);
            prevSum = curSum;
        }
    }

    long min_e = LONG_MAX;
    for (int i=0; i<N; i++) {
        long s = maxLead[i][0];
        long b = maxLead[i][1];
        long l = maxLead[i][2];
        long u = maxLead[i][3];

        long num_line = 0;
        long left_s = 0;
        // Case 0
        if (s >= border) {
            num_line = 0;
            left_s = border;
        } else {
            // Case pos left
            if (sumMaxLead[i] >= border) {
                int p = lower_bound(sumMaxLead.begin(), sumMaxLead.end(), border - s) - sumMaxLead.begin();
                num_line = p + 1;
                left_s = border - sumMaxLead[p];
            // Case pos right
            } else {
                int p = lower_bound(sumMaxLead.begin(), sumMaxLead.end(), border) - sumMaxLead.begin();
                num_line = p;
                left_s = border - (sumMaxLead[p] - s);
            }
        }

        long e = num_line * X;
        if (left_s <= 0) {
            e = e;
        } else if (left_s <= b * l) {
            e += (left_s-1)/l + 1;
        } else {
            e += b + (left_s - b * l - 1)/u + 1;
        }
        min_e = min(min_e, e);
        //cout << "i: " << i << ", b: " << b << ", l: " << l << ", u: " << u << ", s: " << s << endl;
        //cout << "left_s: " << left_s << ", num_line: " << num_line << ", min_e: " << min_e << endl;
    }

    cout << min_e << endl;
}

