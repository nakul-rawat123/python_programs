def armstrong(num):
    list_num = list(str(num))
    num_length = len(list_num)
    value = 0
    for i in range(num_length):
        a = int(list_num[i])
        value += a ** len(list_num)
    if value == num:
        print('it is an armstrong number')
    else: print('it is not an armstrong number')
number = int(input('a number: '))
armstrong(number)