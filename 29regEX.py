from re import *
txt = "My name is Nakul, I am 12 years old"
print(search("^My.*Old$", txt))
print(findall('N...l', txt))
print(findall('N.*l', txt))
print(findall('N.{3}l', txt))
print(findall('\d', txt))
print(findall('Ram|Nakul', txt))
print(findall('\AMy', txt))
print(findall(r'ame\B', txt))
print(findall('\s', txt))
print(findall('\S', txt))
print(findall('[Nna2pqr]', txt))
print(search('Nakul' and 'old', txt))
for i in range(1,10):
    X = split('\s', txt, i)
print(X)
txt = "The rain in Spain"
x = search(r"\bS\w+", txt)
print(x.group())
x = search(r"\bS\w+", txt)
print(x.string)
x = search(r"\bS\w+", txt)
print(x.span())