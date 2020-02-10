txt = open('C:\\prog\\text3.txt', 'r')
txt1 = txt.read()
#print(type(txt1))


# ---------------убираем запятые
nocomma = ''
for i in range(len(txt1)):
    if txt1[i] != ',':
         nocomma = nocomma + txt1[i]
#print(nocomma)


#_------------- формируем list со словами
list_txt = nocomma.split()
#print(list_txt)
# ------------- приводим к нижнему регистру
#list_txt = map(list_txt.lower, )
lower_text = []

######################## верно:
for s in range(len(list_txt)):
     lower_text.append(list_txt[s].lower())

########################

#lower_text = map(str, list_txt[:])
# print(lower_text)


# -------------- словарь с ключами - словами, значения - кол-во
# ----- просто словарь из листа
# dict_txt = {}
# for i in range(len(lower_text)):
#     dict_txt [i] = lower_text[i]
# print(dict_txt)

# ----- задача


dict_txt = {}
for i in range(len(lower_text)):
     dict_txt[lower_text[i]] = lower_text.count(lower_text[i])
print(dict_txt)

# ------------- 5 наиболее встречающихся слов, количество разных слов








