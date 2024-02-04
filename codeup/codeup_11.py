#93-1
n = int(input())
a = input().split()    

for i in range(n):   
    a[i] = int(a[i])

for i in range(n-1, -1, -1):  
    print(a[i], end=' ')

#93-2
n = int(input())
a = list(map(int, input().split()))    # list()... 리스트 생성

for i in reversed(a):    # reversed()... 역순으로!
    print(i, end=' ')

#94-1
n = int(input())
a = list(map(int, input().split()))

min = a[0]
for i in range(n):
    if a[i] < min:
        min = a[i] 

print(min)

#94-2
n = int(input())
a = list(map(int, input().split()))

min = min(a)    # min()... 리스트에서의 최소값 찾기
print(min)

