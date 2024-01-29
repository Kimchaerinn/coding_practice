#61
a, b = map(int, input().split())
print(a | b)    # |...비트 단위로 or 연산

#62
a, b = map(int, input().split())
print(a ^ b)    # ^...비트 단위로 xor 연산

#63
a, b = map(int, input().split())
print(a if a>=b else b)    #3항 연산... x(참이면) if C else y(거짓이면)

#64
a, b, c = map(int, input().split())
d = a if a < b else b
e = d if d < c else c
print(e)

#65
a, b, c = map(int, input().split())

if a % 2 ==0:
    print(a)

if b % 2 ==0:
    print(b)

if c % 2 ==0:
    print(c)

#66-1
a, b, c = map(int, input().split())

print("even" if a % 2 ==0 else "odd")
print("even" if b % 2 ==0 else "odd")
print("even" if c % 2 ==0 else "odd")

#66-2
arr = map(int, input().split())

for i in arr:   #for문 이용
    print("even" if (i % 2 == 0) else "odd")

#67
num = int(input())

if num < 0:    #if (num < 0) and (num % 2 == 0)로 중첩 가능
    if num % 2 == 0:
        print("A")
    else:
        print("B")
else:
    if num % 2 == 0:
        print("C")
    else:
        print("D")

#68-1
score = int(input())

if 90 <= score <= 100:
    print("A")
elif 70 <= score <= 89:
    print("B")
elif 40 <= score <= 69:
    print("C")
elif 0 <= score <= 39:
    print("D")

#68-2
score = int(input())

if score >= 90:
    print("A")
elif score >= 70:
    print("B")
elif score >= 40:
    print("C")
else:
    print("D")

#69
char = input()

if char == "A":
    print("best!!!")
elif char == "B":
    print("good!!")
elif char == "C":
    print("run!")
elif char == "D":
    print("slowly~")
else:
    print("what?")

#70-1
month = int(input())

if month == 12 or month == 1 or month ==2:  #각각 변수와 비교해야함, month==12 or 1 or 2... 이러면 ㄴㄴ
    print("winter")
elif month == 3 or month == 4 or month == 5:
    print("spring")
elif month == 6 or month == 7 or month == 8:
    print("summer")
else:
    print("fall")

#70-2
a = int(input())

#수들의 특징을 관찰하고 이용하자!
if a // 3 == 1:
    print("spring")
elif a // 3 == 2:
    print("summer")
elif a // 3 == 3:
    print("fall")
else:
    print("winter")

