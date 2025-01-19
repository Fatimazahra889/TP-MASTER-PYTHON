def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return "invalid input"

print(convert_to_int(1.2))
print(convert_to_int("allo"))