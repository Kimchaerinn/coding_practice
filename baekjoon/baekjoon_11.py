#10810
n, m = map(int, input().split())
d = [0] * n    

for ball in range(m):
    i, j, k = map(int, input().split())
    for ball in range(i-1, j):    
        d[i-1] = k  
        i += 1

print(*d)


#10813
n, m = map(int, input().split())
d =[]

for ball in range(1, n+1):
        d.append(ball)

for ball in range(m):
    i, j = map(int, input().split())
    temp = d[i-1]
    d[i-1] = d[j-1]
    d[j-1] = temp

print(*d)


#5597-A
d = []
for student in range(1, 31):
    d.append(student)
    
for student in range(28):  
    num = int(input())    
    d.remove(num)         

print(min(d))
print(max(d))


#5597-B    # 간략하게 표현 가능
d = [i for i in range(1,31)]

for i in range(28):
    d.remove(int(input()))  

print(*d)


