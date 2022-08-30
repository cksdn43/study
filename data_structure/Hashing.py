class Dictionary:
    def __init__(self, size):
        self.M = size  # 테이블 크기
        self.keyList = [None]*size
        self.valueList = [None]*size
        self.N = 0  # 저장된 항목 수

    def hashFunc1(self, key):  # 해싱 1함수 연산입니다.
        return key % self.M

    def hashFunc2(self, key):  # 해싱 2함수 연산입니다.
        return self.R - (key % self.R)

    def put1(self, key, value):  # 삽입: 선형조사
        initialPos = self.hashFunc1(key)
        i = initialPos
        while True:
            if self.keyList[i] == None:
                self.keyList[i] = key
                self.valueList[i] = value
                self.N += 1
                return
            if self.keyList[i] == key:
                self.valueList[i] = value
                return
            i = (i + 1) % self.M
            if i == initialPos:
                return

    def get1(self, key):  # 검색(탐색) 선형조사
        initialPos = self.hashFunc1(key)
        i = initialPos
        while self.keyList[i] != None:
            if self.keyList[i] == key:
                return self.valueList[i]
            i = (i+1) % self.M
            if i == initialPos:
                return None

    def remove1(self, key):  # 삭제: 선형조사
        initialPos = self.hashFunc1(key)
        i = initialPos
        while self.keyList[i] != None:
            if self.keyList[i] == key:
                self.valueList[i] = None
                self.keyList[i] = None
                self.N -= 1
                return
            i = (i+1) % self.M
            if i == initialPos:
                return None

    def put2(self, key, value):  # 삽입: 제곱조사
        initialPos = self.hashFunc1(key)
        i = initialPos
        j = 0
        while True:
            if self.keyList[i] == None:
                self.keyList[i] = key
                self.valueList[i] = value
                self.N += 1
                return
            if self.keyList[i] == key:
                self.valueList[i] = value
                return
            j += 1
            i = (initialPos + j*j) % self.M
            if self.N > self.M:
                return

    def get2(self, key):  # 검색: 제곱조사
        initialPos = self.hashFunc1(key)
        i = initialPos
        j = 0
        while self.keyList[i] != None:
            if self.keyList[i] == key:
                return self.valueList[i]
            j += 1
            i = (initialPos + j*j) % self.M
        return None

    def remove2(self, key):  # 삭제함수
        initialPos = self.hashFunc1(key)
        i = initialPos
        j = 0
        while self.keyList[i] != None:
            if self.keyList[i] == key:
                self.valueList[i] = None
                self.keyList[i] = None
                self.N -= 1
                return
            j += 1
            i = (initialPos + j*j) % self.M
        return None

    def put3(self, key, value):  # 입력 이중해싱
        initialPos = self.hashFunc1(key)
        SecondPos = self.hashFunc2(key)
        i = initialPos
        j = 0
        while True:
            if self.keyList[i] == None:
                self.keyList[i] = key
                self.valueList[i] = value
                self.N += 1
                return
            if self.keyList[i] == key:
                self.valueList[i] = value
                return
            j += 1
            i = (initialPos + j*SecondPos) % self.M
            if self.N > self.M:
                return

    def get3(self, key):  # 검색(탐색)함수
        initialPos = self.hashFunc1(key)
        SecondPos = self.hashFunc2(key)
        i = initialPos
        j = 0
        while self.keyList[i] != None:
            if self.keyList[i] == key:
                return key, self.valueList[i]
            j += 1
            i = (initialPos + j*SecondPos) % self.M
        return None

    def remove3(self, key):  # 삭제함수
        initialPos = self.hashFunc1(key)
        SecondPos = self.hashFunc2(key)
        i = initialPos
        j = 0
        while self.keyList[i] != None:
            if self.keyList[i] == key:
                self.valueList[i] = None
                self.keyList[i] = None
                self.N -= 1
                return
            j += 1
            i = (initialPos + j*SecondPos) % self.M
        return None
