def reverseSentence(s):
    s = s.split(" ")
    a = list(s)
    a.reverse()
    for i in a:
        print(i, end = ' ')
