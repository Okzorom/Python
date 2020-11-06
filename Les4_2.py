my_list = [1, 144 , 11, 811, 2, 4, 6]
new_list = [num for i, num in enumerate(my_list) if my_list[i] > my_list[i-1] and my_list[i] != 0]
print(new_list)