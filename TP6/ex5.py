def process_input(user_input):
    try:
        return int(user_input)/10
    except ValueError:
        return "invalid input"
    except ZeroDivisionError:
        return "invalid division"
 
    
print(process_input(1.32))