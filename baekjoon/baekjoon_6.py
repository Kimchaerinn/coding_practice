#2739  
n = int(input())

for i in range(1, 10):
    print(n, "*", i, "=", n*i)

#10950
t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(a+b)

    
#8393-A
n = int(input())
sum = 0

for i in range(n+1):
    sum += i

print(sum)

#8393-B    # 식을 세워서 풀이
n=int(input())

print(n*(n+1)//2)


#25304
x = int(input())    
n = int(input())
sum = 0

for i in range(n):
    a, b = map(int, input().split())
    sum += a*b 

if x == sum:
    print("Yes")
else:
    print("No")