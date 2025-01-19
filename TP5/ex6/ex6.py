import os
with open('TP5/ex6/phrases.txt', 'w') as file:
    file.write("hello")
os.rename('TP5/ex6/phrases.txt', 'TP5/ex6/anciennes_phrases.txt')
with open('TP5/ex6/anciennes_phrases.txt', 'a') as file:
    file.write("\nnew")
print("file renamed successfully")
os.remove('TP5/ex6/anciennes_phrases.txt')
print("file deleted successfully")