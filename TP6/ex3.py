def read_file(filename):
    livres=["jump","surrounded by idiots","the unforgivable"]
    try:
        if filename not in livres:
            raise FileNotFoundError
        return f"the file {filename} exists"
    except FileNotFoundError:
        return f"the file {filename} does not exist"
    
print(read_file("jump"))
print(read_file("the rich dad poor dad"))
