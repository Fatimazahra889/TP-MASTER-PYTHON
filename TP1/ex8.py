def somme_varargs(*args):
    return sum(args)
A ={1,2,3,4}
print(somme_varargs(*A))