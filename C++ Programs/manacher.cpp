#include <bits/stdc++.h>
using namespace std;

#define endl "\n"

int main() {

	string s;
	cin >> s;
	int len = 2 * (int)s.length() + 1, i = 0;
	char newS[len];
	vector<int> p(len, 0);

	newS[i++] = '@';
	for (char ch : s) {
		newS[i++] = ch;
		newS[i++] = '@';
	}

	for (int j = 0, c = 0, r = 0; j < len; j++) {
		int mi = c - (j - c);
		if (j < r) p[j] = min(r - j, p[mi]);
		int right = j + p[j] + 1, left = j - (p[j] + 1);

		while (right < len && left >= 0 && newS[left] == newS[right]) {
			p[j]++;
			right++;
			left--;
		}

		if (j + p[j] > r) {
			c = j;
			r = j + p[j];
		}
	}
	i = 0;
	int index = 0;
	for (int j = 0; j < len ; j++) {
		if (p[j] > i) {
			i = p[j];
			index = j;
		}
	}
	for (int j = index - i; j < index + i; j++) {
		if (newS[j] != '@') cout << newS[j];
	}

	return 0;
}