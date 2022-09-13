#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s1 = "Good";
    string s2 = "Morning";
    string s3 = s1 + " " + s2 + "!";
    cout << s3 << endl;

    s1 = "사과";
    s2 = s1 + " " + to_string(10) + "개";
    cout << s2 << endl;

    return 0;
}