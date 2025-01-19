def get_positive_integer():
    num=int(input("enter a positive number:"))
    while True:
        try:
            if num>=0:
                return f"the number {num} is positive"
            else:
                num=int(input("enter a positive number:"))
        except ValueError:
            return "invalid input"

print(get_positive_integer())
    