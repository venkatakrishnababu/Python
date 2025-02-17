def decor(func):
    def inner(name):
        if name.isupper():
            print(name.lower())
            return
        return func(name)
    return inner
@decor
def convert(name):
    print(name.upper())
S=input('enter a name')
convert(S)