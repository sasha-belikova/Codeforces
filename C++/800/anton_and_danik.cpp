#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    string s;
    cin >> s;

    int anton = 0;
    int danik = 0;

    for (char person : s){
        if (person == 'A'){
            anton +=1; 
        }
        else {
            danik +=1;
        }
    }

    if (anton > danik){
        cout << "Anton";
    }
    else if (anton < danik){
        cout << "Danik";
    }
    else {
        cout << "Friendship";
    }
    
    return 0;
}