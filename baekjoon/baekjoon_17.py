#10988 
word = input()

if word[::1] == word[::-1]:
    print(1)
else:
    print(0)


#1157
word = input().lower()
word_list = list(set(word))
cnt = []

for i in word_list:
    cnt.append(word.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))].upper())
