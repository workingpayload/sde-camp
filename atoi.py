def atoi(string,num):
    if len(string)==1:
        return int(string) + (num*10)

    num = int(string[0:1]) + (num*10)

    return atoi(string[1:],num)


n = str(input())
print(atoi(n,0))
