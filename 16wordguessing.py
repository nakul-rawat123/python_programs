import random as rn
words = ['apple','ball','cat','dog','rahul']
word = rn.randint(0,5)
while True:
    guess = input('your word guess: ')
    if guess == words[word]:
        print('your guess is correct')
        break
    else:
        print('your guess is wrong, try again')