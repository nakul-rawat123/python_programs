from package1.__init__ import *
while True:
    print('what do u want to do:-')
    print('addition - 1, subraction - 2, multiplication - 3, division - 4, check if even or odd - 5')
    op = int(input('your choice: '))
    if op == 5:
        even_odd()
    if op == 4:
        divide()
    if op == 3:
        multiply()
    if op == 2:
        subtract()
    if op == 1:
        add()