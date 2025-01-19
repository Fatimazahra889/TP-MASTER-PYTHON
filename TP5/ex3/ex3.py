def get_sentences():
    sentences = []
    for i in range(1, 4):
        sentence = input(f"Enter sentence {i}: ")
        sentences.append(sentence)
    return sentences

def append_sentences(file_path):
    while True:
        add_more = input("Do you want to add more sentences? (yes/no): ").strip().lower()
        if add_more == 'yes':
            sentence = input("Enter a sentence: ")
            with open(file_path, 'a', encoding=None, errors=None) as file:
                file.write(sentence + '\n')
        elif add_more == 'no':
            break
        else:
            print("Please answer with 'yes' or 'no'.")

# Initial sentences
file_path = 'D:/study/master/PYTHON/TP/TP5/ex2/phrases.txt'
sentences = get_sentences()

# Write initial sentences to the file
with open(file_path, 'w', encoding=None, errors=None) as file:
    for sentence in sentences:
        file.write(sentence + '\n')

# Ask if the user wants to add more sentences
append_sentences(file_path)

print("Sentences have been saved to phrases.txt")