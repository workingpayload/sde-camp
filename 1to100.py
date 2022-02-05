n = 1


def f1(a):
    if a<=100:
        print(a,end=" ")
    a = a+1
    f1(a)


f1(n)
