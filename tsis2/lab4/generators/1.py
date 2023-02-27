class squareS():
    def __init__(self,n):
        self.end = n
        self.start = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.start > self.end):
            raise StopIteration()
        else:
            b = self.start
            self.start += 1
            return b * b
    
n = int(input())

for i in squareS(n):
    print(i)
