def factorial(n):
    if n == 1:
        return n
    else: 
        return n*factorial(n-1)
n = int(input('enter a number: '))
if n < 0:
    print("sorry, factorials of negetive numbers don't exist")
elif n == 0:
    print("factorial of 0 is 1")
else:
    print(f'factorial of {n} is {factorial(n)}')