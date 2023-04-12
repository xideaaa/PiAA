class MyList:
    def __init__(self):
        self.data = []

    def get(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data[index]

    def search(self, value):
        for i in range(len(self.data)):
            if self.data[i] == value:
                return i
        return -1

    def insert(self, index, value):
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of range")
        self.data.insert(index, value)

    def remove(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        self.data.pop(index)

