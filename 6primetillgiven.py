def prime(num):
    primes = []
    for i in range(2,num+1):
        for j in range(2,i):
            if i % j == 0:
                print(i, 'is not prime')
                break
        else:
            print(i, 'is prime')          
number = int(input("range of numbers: "))
print("1 is special")
prime(number)