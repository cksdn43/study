#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    int tower[n + 1];
    int a, b, max;

    for (int i = 0; i < k; i++)
    {
        cin >> a >> b;
        for (int e = a; e <= b; i++)
        {
            tower[e] += 1;
        }
    }
    max = 0;
    for (int i = 0; i <= n; i++)
    {
        if (max < tower[i])
        {
            max = tower[i];
        }
    }
    cout << max;

    return 0;
}