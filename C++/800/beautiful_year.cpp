#include <iostream>
#include <string>
using namespace std;

int main() {
    int y;
    cin >> y;

    while (true) {
        y++;

        string s = to_string(y);
        bool unique = true;

        for (int i = 0; i < s.size(); i++) {
            for (int j = i + 1; j < s.size(); j++) {
                if (s[i] == s[j]) {
                    unique = false;
                }
            }
        }

        if (unique) {
            cout << y << endl;
            break;
        }
    }

    return 0;
}