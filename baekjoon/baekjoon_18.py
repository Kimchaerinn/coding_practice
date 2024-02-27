#2941
word = input()
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alphabet:
    word = word.replace(i, '*')    # repace()... 기존문자를 다른 문자로 대체
        
print(len(word))


#1316
n = int(input())
count = n

for i in range(n):
    word = input()
    for j in range(len(word)-1):    
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            count -= 1
            break
        
print(count)
