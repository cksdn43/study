p = [1, 2, 2, 4, 7, 4, 4, 2, 8]

# 트리를 이용한 집합처리 알고리즘


def Make_Set(x):  # 집합 생성
    p[x] = x


def Union(x, y):  # 합집합 생성
    p[Find_Set(y)] = Find_Set(x)


def Find_Set(x):  # 대표원소로 집합 찾기
    if x == p[x]:
        return x
    else:
        return Find_Set(p[x])

# rank를 이용


rank = []


def Make_Set2(x):
    p[x] = x
    rank[x] = 0


def Union2(x, y):
    x2 = Find_Set2(x)
    y2 = Find_Set2(y)

    if rank[x2] > rank[y2]:
        p[y2] = x2
    else:
        p[x2] = y2
        if rank[x2] == rank[y2]:
            rank[y2] = rank[x2] + 1


def Find_Set2(x):
    if p[x] != x:
        p[x] = Find_Set2(p[x])
    return p[x]
