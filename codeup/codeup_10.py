#91
a, b, c = map(int, input().split())

d = 1
while d%a!=0 or d%b!=0 or d%c!=0:
    d += 1
print(d)

#92
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

d = []    # 빈 리스트 생성
for i in range(24):
    d.append(0)    # d 리스트에 값을 추가하여 넣음

for i in range(n):    # 번호 부를 때마다 카운트 1 증가
    d[a[i]] += 1

for i in range(1, 24):
    print(d[i], end=' ')