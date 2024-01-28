#51
a, b = map(int, input().split())
print(a != b)

#52
n = int(input())    # bool까지 함께 처리해도 됨
print(bool(n))    # bool()...식/값을 평가 > 참 or거짓 판단

#53-1
n = int(input())

if n == 0:
    print("True")
else:
    print("False")

#53-2
a = bool(int(input()))
print(not a)    # not...논리값을 역으로 바꿈

#54
a, b = map(int, input().split())
print(bool(a and b))

#55
a, b = map(int, input().split())
print(bool(a or b))

#56-1
a, b = map(int, input().split())
a, b = bool(a), bool(b)

if a != b:
    print("True")
else:
    print("False")

#56-2
a, b=input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

#57-1
a, b = map(int, input().split())
a, b = bool(a), bool(b)

if a == b:        # print(a==b)      
    print("True")
else:
    print("False")

#57-2
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and b) or (not a and not b))


#58
a, b = map(int, input().split())
a, b = bool(a), bool(b)

print(not a and not b)    # print(not (c or d))

#59
n = int(input())
print(~n)   # ~...입력된 정수를 비트단위로 참/거짓을 바꿈

#60
a, b = map(int, input().split())
print(a & b)

