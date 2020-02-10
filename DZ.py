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
#print(type(list_txt))
# ------------- приводим к нижнему регистру
#list_txt = map(list_txt.lower, )
lower_text = []

######################## верно:
for s in range(len(list_txt)):
    lower_text[s] = list_txt[s].lower()

########################

#lower_text = map(str, list_txt[:])
#print(type(lower_text))


# -------------- словарь с ключами - словами, значения - кол-во
dict_txt = {}
for i in range(len(lower_text)):
    dict_txt [i] = lower_text[i]
print(dict_txt)




