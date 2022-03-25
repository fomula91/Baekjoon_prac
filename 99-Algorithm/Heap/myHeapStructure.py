class Heap:
    def __init__(self):
        self.item = [None]
    def __len__(self):
        return len(self.item) - 1
    def insert(self, value):
        self.item.append(value)
        self.sortUp()

    def extract(self):
        result = self.item[1]
        self.item[1] = self.item[-1]
        self.item.pop()
        self.sortDown(1)
        return result

    def sortUp(self):
        curValue = len(self.item)
        parenValue = curValue // 2
        while parenValue > 0:
            if self.item[curValue] > self.item[parenValue]:
                self.item[curValue], self.item[parenValue] = self.item[parenValue], self.item[curValue]
            curValue = parenValue
            parenValue = curValue // 2

    def sortDown(self, index):
        biggest = index
        left = 2 * index
        right = 2 * index + 1
        if left <= len(self.item) and self.item[left] > self.item[biggest]:
            biggest = left
        if right <= len(self.item) and self.item[right] > self.item[biggest]:
            biggest = right
            self.sortDown()