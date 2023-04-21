class A:
    def greet(a):
        print('hello', a, 'hope you are doing well')
    def response():
        condition = input()
        if condition == 'i am well':
            print('good to hear')
        else: print('get well soon')
    def leave():
        leave = input('do you want to leave')
        if leave == 'yes':
            print('bye have a nice day')
        else: print('how may i help you')
    def ask():
        ques = input()
        if ques == 'how is the weather':
            print('today will be warm and sunny with soem chances of rainfall')
        if ques == 'tell me a joke':
            print('a joke')
        else: print('i do not know how to respont to')
name = input('what is your name')
while True:
    A.greet(name)
    A.response()
    A.ask()
    if A.leave() == 'bye have a nice day':
        break
    else:
        while True:
            A.ask()