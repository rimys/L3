# arr = [1, 2, 3, 1, 2, 3 ,4]
# print(set(arr))
#
# arr2 = set(arr)
# print(type(arr2), arr2)
# tmp_list = [1, 2, 3]
# tmp_tuple = tuple(tmp_list)
# print(type(tmp_tuple), tmp_tuple)
#
# # for i in range(len(tmp_tuple)):
# #     print(tmp_tuple[i])
# #
#
# tmp_list = [1, 2, 3]
#
# print(tmp_tuple.__sizeof__())
# print(tmp_list.__sizeof__())


tmp_set = {2, 1, 3, 44, 0, 22, 3}
tmp_set2 = set ([2, 3, 5, 55, 44])
print(type(tmp_set), tmp_set)

for element in tmp_set:
    print(element)

tmp_set = tmp_set.union(tmp_set2)

print(tmp_set )
