class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, data): # 8
        self.items.append(data) #[10,7,8,5,11]

    def addFront(self, data): #7
        self.items.insert(0, data) # [10,7,8,5]

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

d = Deque()
d.addRear(8) 
d.addRear(5)
d.addFront(7)
d.addFront(10)
d.addRear(11)
print(d.removeRear()) #[10,7,8,5]
print(d.removeFront()) #[7,8,5]
d.addFront(55) #[55,7,8,5]
d.addRear(45) #[55,7,8,5,45]
print(d.items)