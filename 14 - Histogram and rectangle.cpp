#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long> gist(n);
    for (int i = 0; i < n; i++) {
        cin >> gist[i];
    }
    vector<int> otv1(n, -1);
    vector<int> otv2(n, -1);
    stack<pair<int, int>> stackk1;
    stack<pair<int, int>> stackk2;
    vector<long> maxx;
    for (int i = 0; i < n; i++) {
        int num1 = gist[i];
        int num2 = gist[n - i - 1];
        while (!stackk1.empty()) {
            if (stackk1.top().second > num1) {
                otv1[stackk1.top().first] = i;
                stackk1.pop();
            } else {
                break;
            }
        }
        stackk1.push(make_pair(i, num1));

        while (!stackk2.empty()) {
            if (stackk2.top().second > num2) {
                otv2[stackk2.top().first] = n - i - 1;
                stackk2.pop();
            } else {
                break;
            }
        }
        stackk2.push(make_pair(i, num2));
    }
    reverse(otv2.begin(), otv2.end());
    for (int i = 0; i < n; i++) {
        int fr = otv1[i];
        int sc = otv2[i];
        if (fr == -1 && sc == -1) {
            maxx.push_back(long(gist[i]) * n);
        } else if (fr == -1) {
            maxx.push_back(long(gist[i]) * (n - sc - 1));
        } else if (sc == -1) {
            maxx.push_back(long(gist[i]) * fr);
        } else {
            maxx.push_back(long(gist[i]) * (fr - sc - 1));
        }
    }
    cout << *max_element(maxx.begin(), maxx.end());
    return 0;
}