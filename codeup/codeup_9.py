#81
n = int(input(), 16)

for i in range(1, 16):  
    print(f"{n:X}*{i:X}={n * i:X}")    # % operator, format() 이용 가능하나
                                       # f-string이 가장 많이 쓰이고 편리함.

#82
n = int(input())

for i in range(1, n+1):
    if i%10 == 3 or i%10 == 6 or i%10 == 9:
        print("X", end = ' ')
    else:
        print(i, end = ' ')

#83
r, g, b = map(int, input().split())

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)

print(r*g*b)

#84
h, b, c, s = map(int, input().split())

MB = h * b * c * s / 8 / 1024 / 1024
print(format(MB, ".1f"), "MB")    # print(f'{MB:.lf} MB')
                                  # round(MB, 1)로 표현 가능

#85
w, h, b = map(int, input().split())

MB = w * h * b / 8 / 1024 / 1024
print(f'{MB:.2f} MB')

#86
n = int(input())
sum = 0
i = 1

while True:
    sum += i
    i += 1
    if sum >= n:
        break
        
print(sum)

#87-1
n = int(input())

for i in range(1, n+1):
    if i%3 != 0:
        print(i, end=' ')

#87-2
n = int(input())

for i in range(1, n+1): 
  if i%3 == 0: 
    continue           # continue...다음 반복 단계로 넘어감
  print(i, end=' ')    # i가 짝수가 아닐 때만 실행

#88-1    
a, d, n = map(int, input().split())

an = a + (n-1) * d    # 일반항을 이용하여 풀면 단순함
print(an)

#88-2
a, d, n = map(int, input().split())

an = a
for i in range(2, n+1):
   an += d

print(an)

#89
a, r, n = map(int, input().split())

an = a * r ** (n-1)    
print(an)

#90
a, m, d, n = map(int, input().split())

for i in range(1, n):
    a = a * m + d

print(a)

