#11
f = input()
f = float(f)
print(f)

#12-1
a = int(input())
b = int(input())
print(a)
print(b)
#a = input()
#a = int()를 합쳐서 표현

#split()처럼 공백이 아닌 엔터를 기준으로 2개를 입력받고 싶었으나 함수가 없음

#13
a=input()
b=input()
print(b)
print(a)

#14
f = float(input())
print(f)
print(f)  
print(f)

#15
a, b = map(int, input().split())
print(a)
print(b)

#16
a, b = input().split()
print(b, a)

#17
a = input()
print(a, a, a)

#18
a, b = input().split(":")
print(a, b, sep = ":")
#split 어떤 기준으로 입력받을지.. 여기선 :
#sep 출력 시 어떤 기준으로 자를지.. 여기선 :

#19
y, m, d = input().split(".")
print(d, m, y, sep = "-")

#20
a, b = input().split("-")
print(a, b, sep = '')
#'' 공백없이 출력
