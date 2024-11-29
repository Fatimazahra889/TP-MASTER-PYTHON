from collections import Counter
def compte_occurences(liste):
    return dict(Counter(liste))
liste=["ema","bro","bro","ema","ema","fati"]
print(compte_occurences(liste))