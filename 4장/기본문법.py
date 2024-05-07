my_dict = {}

my_dict['apple'] = 1
my_dict['banana'] = 2
my_dict['orange'] = 3
print(my_dict)

key = 'apple'
if key in my_dict:
    value = my_dict[key]
    print(f'{key}:{value}')
else:
    print(f'{key}는 딕셔너리에 없습니다')
    
my_dict['banana'] = 4
print(my_dict)

del my_dict['orange']
print(my_dict)

my_dict = {'apple':1, 'banana':2, 'cherry':3}

key = 'kiwi'

if key in my_dict:
    value = my_dict['key']
    print(f'{key}:{value}')
else:
    print(f'{key}가 없습니다')
    
my_tuple = (1, 2, 3)
print(my_tuple[0])
print(my_tuple[-1])

string = 'He'
string += 'llo'
print(string)

string = 'Hello'
string = string.replace('l', '')
print(string)

def add(num1, num2):
    return num1 + num2

ret = add(1, 2)
print(ret)

add = lambda a, b : a+b
print(add(2,5))

num = [1, 2, 3, 4, 5]
squares = list(map(lambda x : x**2, num))
print(squares)
