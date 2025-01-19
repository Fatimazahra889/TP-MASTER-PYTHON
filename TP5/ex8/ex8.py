try:
    with open('TP5/ex8/inexistant.txt','r') as file:
        print(file.read())
except FileNotFoundError:
    print('doesnt exist')

