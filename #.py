class int_():
    def __init__(self):
        print('the number is an integer')
a = int(input('a number: '))
if type(a) == int:
    a = int_()