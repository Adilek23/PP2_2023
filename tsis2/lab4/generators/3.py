class divisible():
    def __init__(self, n):
        self.start = 0
        self.end = n

    def __iter__(self):
        return self
    
    def __next__(self):
        if(self.start <= self.end):
            b = self.start
            self.start += 1
            if (b % 3 == 0 and b % 4 == 0):
                return b
            
        else :
                raise StopIteration()
            
        
        
n = int(input())
for i in divisible(n):
    if(i != None):
        print(i)