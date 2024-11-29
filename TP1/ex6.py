def carre():
    return lambda x :x**2

a= int(input("enter a number : "))
result =carre() 
print(result(a))
    