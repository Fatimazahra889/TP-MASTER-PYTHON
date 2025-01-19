import shutil
with open('TP5/ex7/journal.txt','w') as f:
    f.write('first line\n')
    f.write('second line\n')
    f.write('third line\n')

shutil.copy('TP5/ex7/journal.txt','TP5/ex7/journal_copie.txt')
shutil.move('TP5/ex7/journal_copie.txt','TP5/ex7/archives/journal_copie.txt')
