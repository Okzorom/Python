from functools import reduce
new_list = [num for num in range(100, 1001) if num%2 ==0]
multiply = reduce(lambda x, y: x*y, new_list)
print(multiply)