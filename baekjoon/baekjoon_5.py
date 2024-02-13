#2884-A
a, b = map(int, input().split())

if b >= 45:
    b -= 45
    
else:
    b = b+60 - 45

    if a == 0:
        a = 23
    else:
        a -= 1

print(a, b)
        
#2884-B    # 연산자 이용. 영리하게 풀자
h, m = map(int, input().split())
result = h*60 + m - 45
print(result//60%24, result%60)    # %24... 시간 범위 0 ~ 23 출력 의도


#2525   
h, m = map(int, input().split())
time = int(input())

min = h*60 + m + time

print(min//60%24, min%60)


#2480-A
x, y, z = map(int, input().split())

if x == y == z:
    money = 10000 + x*1000
elif x == y or x == z:
    money = 1000 + x*100
elif y == z:
    money = 1000 + y*100
else:
    max = x        # money = max(x, y, z) * 100
    if max < y:    # > max()... 최댓값 찾기 가능
        max = y
    if max < z:
        max = z
    money = max * 100

print(money)

#2480-B    # sorted() 이용... 오름차순 정렬 가능
x, y, z = sorted(map(int,input().split()))

if x == z:
    print(10000 + x*1000)
elif x == y or y == z:
    print(1000 + y*100)
else:
    print(z * 100)


