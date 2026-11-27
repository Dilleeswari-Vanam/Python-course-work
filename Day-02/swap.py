a=10
b=20
print('a:',id(a))
print('b:',id(b))
a,b=b,a
print(a,b)
print('a:',id(a))
print('b:',id(b))
