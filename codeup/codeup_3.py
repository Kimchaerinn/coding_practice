#21-1
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

#21-2
s = input()
for i in range(0,5):
    print(s[i])

#22
s = input()
print(s[0:2], s[2:4], s[4:6])   #s[4:]라고 표현해도 됨
#공백 구분이 아닐 수 있으니 ,sep = ''를 뒤에 추가해주는 것도 좋음

#23
h, m, s = input().split(":")
print(m)

#24-1
w1, w2 = input().split()
print(w1, w2, sep = '')

#24-2
w1, w2 = input().split()
s = w1 + w2
print(s)

#25-1
x, y = map(int, input().split())
print(x +y)

#25-2
a, b = input().split()
c = int(a) + int(b)
print(c)

#26
x = float(input())
y = float(input())
print(x + y)

#27
a = int(input())
print('%x' %a)

#28
a = int(input())
print("%X" %a)

#29
a = int(input(), 16)
print("%o" %a)

#30
a = ord(input())    #ord... 입력받은 문자를 10진수 유니코드 값으로 변환
print(a)



