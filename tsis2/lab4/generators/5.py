def retur(n):
    while (n > 0):
        yield n
        n -= 1

n = int(input())
for i in retur(n):
    print(i)