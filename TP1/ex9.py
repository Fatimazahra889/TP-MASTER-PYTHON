def analyse_texte(texte):
    word= texte.split()
    word_len={word:len(word) for word in word}
    return "number of characters:"+"" +str(len(texte)) +"\nnumber of words:"+""+ str(len(word))+"\n"+str(word_len)
a=str(input("enter a phrase :"))
print(analyse_texte(a))