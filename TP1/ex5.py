def factorielle(n):
    if n==0:
        return 1
    else :
        for i in range (1,n):
            n= n*i
        return n
a = int(input("enter a number :"))
print(factorielle(a)) 