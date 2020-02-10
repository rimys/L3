

list_1 = []         #пустой список
#print(type(list_1))
list_1 = [1.2, 123, 'aaaa', [1,2,3]]

# for el in list_1:

# print()
# list_str = list('slovo ne varabei')
# # print(list_str)
#
# for i in range(len(list_1)):
#     print(i+1, ':', list_1[i])
# for i in range(len(list_1)):
#     print(i+1, ':', list_1[i:])
# for i in range(len(list_1)):
#     print(i+1, ':', list_1[:i])
#
#
# print(len(list_1))
#
# print(list_1 + list_str)
# print(list_1*2)

int_list = []
for i in range (20):
    int_list.append(i)
print(int_list)
int_list.append(100)
int_list.append(0)
print(int_list)

int_list.remove(0)
print(int_list)
del int_list[3]
print(int_list)
int_list.reverse()
print(int_list)

int_list = [4, 5, 2, 7, 1, 8, 222]
int_list.sort()
print(int_list)

int_list.insert(4, 111)
print(int_list)
