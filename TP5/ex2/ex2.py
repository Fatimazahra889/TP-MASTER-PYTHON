sentences = []
for i in range(1, 4):
    sentence = input(f"Enter sentence {i}: ")
    sentences.append(sentence)

with open('D:/study/master/PYTHON/TP/TP5/ex2/phrases.txt', 'w', encoding=None, errors=None) as file:
    for sentence in sentences:
        file.write(sentence + '\n')

print("Sentences have been saved to phrases.txt")