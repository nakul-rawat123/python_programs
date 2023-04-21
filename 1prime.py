def prime(num):
    for i in range(2,num):
        if num%i == 0:
            print('number is not prime')
            break
    else: print('number is prime')
num = int(input('a number'))
prime(num)