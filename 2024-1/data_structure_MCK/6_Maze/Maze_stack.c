#include<stdio.h>
#include<stdlib.h>

#define ROWS 5
#define COLS 7

// 미로 ('0'은 길, '1'은 벽, 'S'는 시작점, 'F'는 목표점)
char maze[ROWS][COLS]={
    {'S','0','0','1','0','0','0'},
    {'1','1','0','1','0','1','0'},
    {'0','0','0','0','1','0','F'},
    {'0','1','1','1','1','0','1'},
    {'0','0','0','0','0','0','1'}
};

typedef struct{
    int x;
    int y;
}Position;

// 스택 정의

Position stack[ROWS * COLS];
int top = -1;

void push(Position pos){
    if(top < (ROWS * COLS) - 1){
        stack[++top] = pos;
    }
}

Position pop(){
    if (top >= 0){
        return stack[top--];
    }
    Position invalid = {-1, -1};
    return invalid;
}

int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

void searchMaze(int startX, int startY){
    push((Position){startX, startY});
    
    while(top != -1){
        Position current = pop();
        int x = current.x, y = current.y;

        // 목표에 도달한 경우
        if(maze[y][x] == 'F'){
            printf("목표에 도달했습니다.\n");
            return;
        }

        // 현재 위치 방문 처리
        maze[y][x] = '1'; // 방문한 길도 벽으로 처리하여 중복 방문 방지

        // 모든 방향에 대하여 탐색
        for(int i = 0; i < 4; i++){
            int nextX = x + dx[i], nextY = y + dy[i];

            // 미로의 범위를 벗어나지 않고, 길이 있는 경우
            if(nextX >= 0 && nextX < COLS && nextY >= 0 && nextY < ROWS && (maze[nextY][nextX] == '0' || maze[nextY][nextX] == 'F')){
                push((Position){nextX, nextY});
            }
        }
    }
    printf("목표점에 도달 할 수 없습니다.\n");
}

int main(void){
    searchMaze(0, 0);
    return 0;
}