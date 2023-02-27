class even():
    def __init__(self, n):
        self.start = 0
        self.end = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.start <= self.end):
            b = self.start
            self.start += 2
            return b
        else :
            raise StopIteration()
n = int(input())

print(*even(n), sep = ',')