'''
#1152
print(len(input().split()))


#2908-A
a, b = input().split()

a = int(a[::-1])    # [::-1]...역순
b = int(b[::-1])

if a > b:
    print(a)    
else:
    print(b)
    
#2908-B
print(max(input()[::-1].split()))


#5622
word = list(input())
result = 0

for i in range(len(word)):
    if 65 <= ord(word[i]) < 68:
        time = 3
    elif ord(word[i]) < 71:
        time = 4
    elif ord(word[i]) < 74:
        time = 5
    elif ord(word[i]) < 77:
        time = 6
    elif ord(word[i]) < 80:
        time = 7
    elif ord(word[i]) < 84:
        time = 8
    elif ord(word[i]) < 87:
        time = 9
    else:
        time = 10
    
    result += time

print(result)

#
'''

#11718
while True:
    print(input())
