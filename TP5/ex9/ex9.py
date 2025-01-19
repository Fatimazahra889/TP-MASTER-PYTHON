word=0
char=0
with open('TP5/ex9/file.txt','r') as file:
    file=file.readlines()
    print(len(file))
    for line in file:
        word +=len(line.split())
        char +=len(line)
print(word)
print(char)       