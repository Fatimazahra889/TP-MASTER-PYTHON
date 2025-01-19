#r = for read 
#encoding = specifies the encoding system , none means choose the default 
#errors =hadnkles the encoding decoding errors 
#closefd= close the file descriptor when the file is closed
with open('exemple.txt','r', encoding=None, errors=None, closefd=True, opener=None) as file:
    # Iterate over each line in the file
    for nm, line in enumerate(file, start=1):
        # Print the line number and the line content
        print(f"{nm}: {line.strip()}")
