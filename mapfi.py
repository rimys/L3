int_list2 = [8, 4, 2, 5, 1]

# new_int_list  = list(map(str, int_list2))

# print(new_int_list)

# for i in range (len(new_int_list)):
#     print(type(new_int_list[i]))
y=0
# int_list2  = list(filter(lambda x: x<5, int_list2))
# print(int_list2)
from functools import reduce
sum = reduce(lambda x,z: x+y, int_list2)
print(sum)