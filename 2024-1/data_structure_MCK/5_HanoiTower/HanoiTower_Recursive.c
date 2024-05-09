#include <stdio.h>

void moveDisk(char fromPeg, char toPeg, int disk){
    printf("원판 %d를 %c에서 %c로 이동\n", disk, fromPeg, toPeg);
}

void hanoiTower(int n, char fromPeg, char auxPeg, char toPeg){// 시, 보, 목
    if(n == 1){
        moveDisk(fromPeg, toPeg, 1);
        return;
    }
    hanoiTower(n-1, fromPeg, toPeg, auxPeg); // 시, 목, 보
    moveDisk(fromPeg, toPeg, n); // 시, 목
    hanoiTower(n-1, auxPeg, fromPeg, toPeg); // 보, 시, 목
} 

int main(){
    int n = 3;
    hanoiTower(n, 'A', 'B', 'C'); // A: 시작기둥, B: 보조기둥, C: 목적지 기둥
    return 0;
}
// 이동 공식 2^n-1