x = int(input())
try:
    print(x)
except:
    print('variable not found')
else:
    print('no error')
finally:
    print('end')