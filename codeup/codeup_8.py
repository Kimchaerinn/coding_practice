#71-1
n = 1
while n != 0:
    n = int(input())    
    if n != 0:
        print(n)
    else:       # 생략 가능
        break
    
#71-2
while True:
    n = int(input())    
    if n != 0:
        print(n)
    else:
        break
        
#72
n = int(input())
while n > 0:    # while n != 0:
    print(n)
    n = n - 1

#73-1   # 2번째 풀이가 더 깔끔함
n = int(input())

while n != 0:
    print(n - 1)
    n = n - 1
    if n == 0:
        break
        
#73-2
n = int(input())

while n != 0:
    n = n - 1
    print(n)
    
#74
c = ord(input())    # ord...문자를 유니코드 정수로
start = ord('a')
while start <= c:
    print(chr(start), end = ' ')    # chr...정수 값을 유니코드 문자로 
    start += 1

#75-1
i = 0
n = int(input())

while i <= n:
    print(i)
    i = i + 1

#76
n = int(input())
for i in range(n + 1):  # range(n)... n-1까지의 수열
    print(i)

#77
n = int(input())
s = 0

for i in range(n + 1):
    if i % 2 == 0:
        s += i
    
print(s)

#78
c = 'c'

while c != 'q':
    c = input()
    print(c)
    if c == 'q':    # 생략 가능
        break
    
#79-1
n = int(input())
i = 1   
sum = 0

while sum < n:  
    sum += i    
    i += 1
    
print(i - 1)    

#79-2
n = int(input())
s = 0
t = 0

while s < n :
  t = t + 1
  s = s + t
  
print(t)

#80
n, m = map(int, input().split())

for i in range(1, n + 1):   # for문 중첩 가능
    for j in range(1, m + 1):
        print(i, j)



