def temp_change(temp):
    new_temp = (temp*(9/5))+32
    return new_temp
temps = [('Berlin', 29),('India', 36),('New York', 31), ('London', 24), ('Tokyo', 27), ('Sydney', 35)]
for i in temps:
    print(f"{i[0]}'s temperature is {temp_change(i[1])} fehrenheit ({i[1]} celcius)")