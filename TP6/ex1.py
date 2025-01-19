def safe_division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "division by zero is not possible"
    
print(safe_division(1,4))
print(safe_division(10.3,0))
