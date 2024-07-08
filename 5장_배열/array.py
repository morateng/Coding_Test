arr = [0, 0, 0, 0, 0, 0]
arr = [0] * 6
print(arr)

arr = list(range(6))
print(arr)

arr = [0 for _ in range(6)]
print(arr)

arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(arr[2][3])

arr = [[i]*4 for i in range(3)]
print(arr)

#-----자주 사용되는 리스트 기법-----
my_list = [1, 2, 3]
my_list.append(4)

my_list = my_list + [6, 7]
print(my_list)

my_list.insert(2, 555)
print(my_list)

popped_element = my_list.pop(2)
print(popped_element)
print(my_list)

my_list = [1, 2, 3, 2, 4, 5]
my_list.remove(2)
print(my_list)

numbers = [1, 2, 3, 4, 5]
sqaures = [num**2 for num in numbers]
print(sqaures)