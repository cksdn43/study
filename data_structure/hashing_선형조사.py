# 해싱 개방주소방식 선형조사
class Dictionary:
    def __init__(self, size):
        self.M = size
        self.keyList = [None] * size
        self.valueList = [None] * size
        self.N = 0

    def hashFunc(self, key):
        return key % self.M

    def put(self, key, value):
        initialPos = self.hashFunc(self, key)
        i = initialPos
        while True:
            if self.keyList[i] == None:
                self.keyList[i] = key
                self.valueList[i] = value
                self.N += 1
                return
            elif self.keyList[i] == key:
                self.valueList[i] = value
                return
            i = (i + 1) % self.M
            if i == initialPos:
                return

    def get(self, key):
        initialPos = self.hashFunc(key)
        i = initialPos
        while self.keyList[i] != None:
            if self.keyList[i] == key:
                return self.valueList[i]
            i = (i + 1) % self.M
            if i == initialPos:
                return
