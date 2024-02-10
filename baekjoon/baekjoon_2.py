#18108
y = int(input())   
result = print(y - 543)


#10430
A, B, C = map(int, input().split())

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)


#2588-A
a = int(input())
b = input()

print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))

#2588-B
a = int(input())    
b = int(input())

print(a*(b%10))
print(a*(b%100//10))
print(a*(b//100))
print(a * b)

