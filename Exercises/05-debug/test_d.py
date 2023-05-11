print('Start programm')

def my_special_function(text, value):
    print(text)
    print('my special function was calles! value=', value)
    inner_function(value)

def inner_function(value):
    print('inner-function is called')
    print(value)

for i in range(10):
    print(i)
    if i==5: 
        my_special_function('i=5',42)