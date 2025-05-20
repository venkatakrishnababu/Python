def converter(func):
    """A decorator to convert the case of a name.
    If the name is all uppercase, it will converts all to lowercase.
    If the name is all lowercase, it will converts all to uppercase.
    Otherwise, it returns the same name
    """
    def wrapper(name):
        if name.isupper():
            return func(name.lower()) #Return lower
        elif name.islower():
            return func(name.upper()) #Return upper
        else:
            return name #Returns same

    return wrapper

@converter
def unchanged_name(name):
    """This function is decorated """
    return name
A=unchanged_name('n')
print(A)