def find_factors(num):
    for i in range(1,num+1):
        if num % i == 0:
            print(i)
number = int(input("a number:"))
find_factors(number)