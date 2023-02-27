def square(n,m):
    
    while (n <= m):
        yield n * n  
        n += 1

n = int(input())
m = int(input())        
for i in square(n,m):
    print(i)