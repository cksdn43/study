# 해싱 개방주소방식 제곱조사
class dictionary:
    def __init__(self, size):
        self.M = size
        self.keyList = [None]*size
        self.valueList = [None]*size
        self.N = 0

    def hashFunc(self, key):
        return key % self.M

    def put(self, key, value):
        initialPos = self.hashFunc(key)
        i = initialPos
        j = 0
        while True:
            if self.keyList[i] == None:
                self.keyList[i] = key
                self.valueList[i] = value
                self.N += 1
                return
            elif self.keyList[i] == key:
                self.valueList[i] = value
                return
            j += 1
            i = (initialPos + j*j) % self.M
            if self.N > self.M:
                return

    def get(self, key):
        initialPos = self.hashFunc(key)
        i = initialPos
        j = 0
        while self.keyList[i] != None:
            if self.keyList[i] == key:
                return self.valueList[i]
            j += 1
            i = (initialPos + j*j) % self.M
        return
