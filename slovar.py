slovar1 = {}
slovar1 = {'a' : 'azbuka', 'b' : 'bukvar'}

print(slovar1)

sl_1 = slovar1.fromkeys(['a' , 'b'], [12 , 1111])

print(type(sl_1), sl_1)

sl_1 = dict(word1 = 'hello')
print(type(sl_1), sl_1)

print(sl_1['word1'])

sl2 = {a: a**2 for a in range(10)}
print(sl2[8])

print(list(sl2.keys()))
print(list(sl2.values()))
print(list(sl2.items()))

sl2[0] = 110
print(sl2)

sl2['num'] = 'stopisot'
print(sl2)

sl2.pop(5)
print(sl2)

for pair in sl2.items():
    print(pair)

for key, value in sl2.items():
    print(key, value)

for key in sl2.values():
    print(key)



