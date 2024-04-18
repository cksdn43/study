#include <stdio.h>

#define MAX_PROCESS 100

// 구조체 프로세스
struct Process{
    int priority;
    int is_target;
};

int Process_runs(int priorities[], int n, int location){
    struct Process queue[MAX_PROCESS];
    struct Process current;
    int count = 0;

    // 큐 초기화
    for(int i = 0; i < n; i++){
        queue[i].priority = priorities[i];
        queue[i].is_target = (i == location);
    }

    while(n>0){
        current = queue[0];
        for(int i = 0; i < n - 1; i++) queue[i] = queue[i + 1]; // 앞으로 밀기
        n--;

        int higher_priority_waiting = 0; // 우선순위 높은 프로세스 처리됨

        for(int i = 0; i < n; i++){
            if(queue[i].priority > current.priority){
                higher_priority_waiting = 1;
                break;
            }
        }
        if(higher_priority_waiting) queue[n++] = current;
        else{
            count++;
            if (current.is_target) return count;
        }
    }
    return -1;
}

int main(){
    int priorities1[] = {2, 1, 3, 2};
    int location1 = 2;
    int n1 = sizeof(priorities1) / sizeof(priorities1[0]);
    printf("%d\n", Process_runs(priorities1, n1, location1));

    int priorities2[] = {1, 1, 9, 1, 1, 1};
    int location2 = 0;
    int n2 = sizeof(priorities2) / sizeof(priorities2[0]);
    printf("%d\n", Process_runs(priorities2, n2, location2));
}