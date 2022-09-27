string = input("enter the string: ")
s = string.split()[::-1]
word = []
for i in s:
    word.append(i)
print(" ".join(word))
