#include <stdio.h>

typedef int element;


int main(void){
    element a[] = {5, 4, 3, 2, 1};
    element n = sizeof(a)/sizeof(int);

    for (int i = 1; i < n; i++){
        element t = a[i];
        int j;
        for(j = i - 1; j >= 0 && t < a[j]; j--)
            a[j+1] = a[j];
        a[j+1] = t;
        
    }
    for(int i = 0; i < n; i++){
        printf("%d ", a[i]);
    }
    return 0;
}

// average O(n^2) best O(n) space O(n) worst comparison count n(n-1)/2