s = list(map(str,input().split()))

l = 0
h = len(s)-1

while l<h:
    temp = s[l]
    s[l] = s[h]
    s[h] = temp
    l+=1
    h-=1

print(s)
