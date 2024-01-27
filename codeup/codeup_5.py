#41
a, b = map(int, input().split()) 
print(a % b)    # %... 나머지 연산자

#42
n = float(input())
print(format(n, ".2f"))    # format(수, ".2f") 원하는 자리까지 반올림

#43
f1, f2 = map(float, input().split())
div = f1 / f2
print(format(div, ".3f"))

#44
a, b = map(int, input().split())
print(a + b) 
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(format(a / b, ".2f"))

#45
a, b, c = map(int, input().split())
sum = a + b + c
average = format(sum / 3, "0.2f")   
print(sum, average)    

#46 -1 
n = int(input())
print(n * 2)

#46 - 2
n = int(input())
print(n << 1)    # <<... 비트시프트 연산(왼쪽: 0 추가(2배), 오른쪽(1/2배))

#47-1
a, b = map(int, input().split())
print(a * (2**b))

#47-2
a, b = map(int, input().split())
print(a << b)

#48-1
a, b = map(int, input().split())
if(a < b):
    print("True")

else:
    print("False")

#48-2
a, b = map(int, input().split())
print(a < b)

#49
a, b = map(int, input().split())
print(a == b)   # 48-1처럼 풀어도 ok

#50
a, b = map(int, input().split())
print(b >= a)   # 이하동일

