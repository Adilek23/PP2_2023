def filter_prime(my_list):
    x = []
    for i in my_list:
        cnt = 0
        if(i == 2):
            x.append(i)
            continue
        elif(i == 1):
            continue
        for j in range(2, i):
            if(i % j == 0):
                cnt += 1
        if(cnt == 0):
            x.append(i)
    return x