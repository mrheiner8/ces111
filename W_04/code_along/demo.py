# Pass by value demo
def add_one(num):
    print(f'num inside function {num}')
    num+=1
    print(f'num inside function after adding 1 is {num}')

var=1
print (f'var before calling function {var}')
add_one(var)
print (f'var after calling function {var}')