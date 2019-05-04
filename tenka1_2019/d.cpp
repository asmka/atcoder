#include<iostream>

using namespace std;


bool check_triangle(int a, int b, int c) {
    if (a+b >= c) {
        return false;
    }
    if (b+c >= a) {
        return false;
    }
    if (c+a >= b) {
        return false;
    }
    return true;
}

int main() {
    int N;
    int a[N];
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> a[i];
    }




}
