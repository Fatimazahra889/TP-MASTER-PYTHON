def safe_division_v2(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Division by zero is not possible"
    else:
        return f"Division is successful:{result}" 
    finally:
        print("Division attempt is complete")

print(safe_division_v2(1, 4))     
print(safe_division_v2(10, 0))      
