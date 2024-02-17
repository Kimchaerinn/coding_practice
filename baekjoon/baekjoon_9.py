#10807
n = int(input())
num = list(map(int, input().split()))
v = int(input())

print(num.count(v))


#10871
n, x = map(int, input().split())
num = list(map(int, input().split()))
d = []

for i in range(len(num)):    # len num > n... 더 간단
    if num[i] < x:
        d.append(num[i])     # print(num[i], end=' ')
                             # > 굳이 리스트 d 만들 필요 없음
print(*d)


