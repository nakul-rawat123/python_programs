import random
value=random.randint(1,100)
while True:
    Input=int(input('your guess: '))
    if Input<value:
        print('value is greater')
    elif Input>value:
        print('value is smaller')
    elif Input==value:
        print('correct answer')
        break