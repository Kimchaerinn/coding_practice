#10818
n = int(input())
num = list(map(int, input().split()))
num.sort()            

print(num[0], num[-1])    # 정렬없이 min(), max() 함수 이용하면 편리


#2562
num = []

for i in range(9):
    n = int(input())    # num.append(int(input()))
    num.append(n)       # > 한 줄로 표현 가능

print(max(num))
print(num.index(max(num))+1)

