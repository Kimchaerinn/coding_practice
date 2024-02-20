#3052
nums = []

for i in range(10):
    nums.append(int(input())%42)

print(len(set(nums)))    # set()... 요소 중복 허용 안 함


#10811
n, m = map(int, input().split())
basket = [i for i in range(1, n+1)]

for i in range(m):
    i, j = map(int, input().split())    
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

print(*basket)