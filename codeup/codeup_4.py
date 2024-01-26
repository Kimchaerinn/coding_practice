#31
c = int(input())
print(chr(c))   # chr... c에 저장된 정수 값 유니코드 문자로 바꿈

#32
c = int(input())
print(-c)

#33
c = ord(input())
print(chr(c+1))

#34
a, b = map(int, input().split())
print(a - b)

#35
f1, f2 = map(float, input().split())
print(f1 * f2)

#36
a, b = input().split()
print(a * int(b))

#37
n = int(input())
s = input() 
print(s * n)

#38
a, b = map(int, input().split())
print(a ** b)

#39
f1, f2 = map(float, input().split())
print(f1 ** f2)

#40
a, b = map(int, input().split())
print(a // b)
