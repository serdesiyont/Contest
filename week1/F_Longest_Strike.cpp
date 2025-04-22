#include <bits/stdc++.h>
using namespace std;

void solve() {
    long long n, k;
    cin >> n >> k;
    
    vector<long long> v(n);
    map<long long, long long> freq;

    for (auto& i : v) {
        cin >> i;
        freq[i]++;
    }

    vector<long long> valid;
    for (auto& [num, count] : freq) {
        if (count >= k)
            valid.push_back(num);
    }

    if (valid.empty()) {
        cout << "-1\n";
        return;
    }

    long long maxLen = -1, l = -1, r = -1;
    long long start = valid[0];

    for (size_t i = 1; i < valid.size(); ++i) {
        if (valid[i] != valid[i - 1] + 1) {
            if (valid[i - 1] - start > maxLen) {
                maxLen = valid[i - 1] - start;
                l = start;
                r = valid[i - 1];
            }
            start = valid[i];
        }
    }

    // Final check for the last segment
    if (valid.back() - start > maxLen) {
        l = start;
        r = valid.back();
    }

    cout << l << ' ' << r << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
