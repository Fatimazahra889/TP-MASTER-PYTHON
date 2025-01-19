import os
file=input("enter the file name:")
try:
    if file in os.listdir():
        with open(file,'r') as f:
            content=f.read()
            print("the file exist and read correctly")
    else:
        raise FileNotFoundError
except FileNotFoundError:
    print("is not read correctly")
try:
    a=int(input("please enter a number:"))
except ValueError:
    print("invalid input")  