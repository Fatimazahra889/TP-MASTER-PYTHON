class NegativeAgeError(Exception):

    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError (f"age invalid:{age}")
    else :
        print("age valid:",age)
    return age
   
ages=[-1,2,3,0]
for ages in ages:
    try:
        result = set_age(ages)
    except NegativeAgeError as e:
        print(e)