# my_string = "semos_ edukacija"
# -> zemi gi poslednite 5 elementi od stringot vo obraten redosled
# print(my_string[len(my_string)-1:len(my_string)-6:-1])

# TUPLES
# count()
# index()

# my_tuple = (1, 2, 3, "apple", 4, 1, "pear")
# counter = my_tuple.count(1)
# index_1 = my_tuple.index(1)

# print(counter, index_1)

# SET
# fruits = {"apple", "pear", "banana"}
# add()
# fruits.add("kiwi")
# print(fruits)
# clear()
# fruits.clear()
# print(fruits)
# copy()
# fruits_copy = fruits.copy()
# print(fruits_copy)
# fruits_copy.add("strawberry")
# difference() -> gi vrakja samo unikatnite elementi od dva seta
# difference = fruits_copy.difference(fruits)
# print(difference)
# difference_update() -> gi zachuvuva samo unikatnite elementi vo prviot set
# fruits_copy.difference_update(fruits)
# print(fruits_copy)
# print(fruits)
# discard()
# fruits.discard("banana")
# intersection() -> gi vrakja zaednichkite elementi megju dva seta
# interesection = fruits.intersection(fruits_copy)
# print(interesection)
# intersection_update() -> gi zachuvava samo zaednichkite elementi vo prviot set
# fruits.add("223")
# fruits.intersection_update(fruits_copy)

# isdisjoint() -> dali se totalno razlichni elementite vo 2 seta
# my_set = {1, 2}
# my_set_2 = {3, 4}
# print(fruits.isdisjoint(fruits_copy))
# print(my_set.isdisjoint(my_set_2))

# print(fruits, fruits_copy)
# issubset()
# print(fruits.issubset(fruits_copy))
# issuperset()
# print(fruits_copy.issuperset(fruits))
# print(fruits.issuperset(fruits_copy))
# pop()
# fruits_copy.pop()
# print(fruits_copy)
# remove()
# fruits.remove("banana")
# fruits.remove("012")

# print(fruits)
# union()
# union = fruits.union(fruits_copy)
# print(union)
# update()
# fruits_copy.add("123")
# fruits.update(fruits_copy)
# print(fruits)
# print(fruits)

# my_dict = {
#     "name": "Tamara",
#     "last_name": "Ilieva",
#     "job_title": "Python Developer",
# }

# print(my_dict["name"])

# clear()
# copy()
# fromkeys()

# lista = ['name', 'lastname', 'phone']
# dict2 = dict.fromkeys(lista, 0)
# print(dict2)

# get()
# print(my_dict.get("last_name"))
# items()
# print(my_dict.items())
# keys()
# print(my_dict.keys())
# pop()
# my_dict.pop("last_name")
# print(my_dict)
# popitem()
# my_dict.popitem()
# print(my_dict)
# setdefault()
# print(my_dict.setdefault("phone_number", "1234567"))
# print(my_dict)
# update()
# my_dict.update({"email": "tamarailieva@live.com"})
# print(my_dict)

# values()
# print(my_dict.values())
# nov_kluch = "adresa"
# print(my_dict.get("adresa")) # -> ako e None ne postoi
# print(my_dict.keys())

# lista = ['name', 'lastname', 'phone']
# if '212423' not in lista:
#     print("elementot ne e prisuten vo listata")


# EXERCISES !!

# Zadacha 1
# Да се напише програма која ќе проверува дали внесениот број е парен или непарен.

# broj = int(input())
# if broj % 2 == 0:
#     print(f"Brojot {broj} e paren")
# else:
#     print(f"Brojot {broj} ne e paren")

# Zadacha 2
# Да се напише програма која го опишува внесениот број. Се внесува цел број (x), тој се проверува и
# се печати соодветниот текст што го опишува бројот, според следната табела (табелата погледнете ја на презентацијата)

# x = int(input())
#
# if x >= 1000:
#     print("Preterano pozitiven")
#
# elif 999 >= x >= 100:
#     print("Mnogu pozitiven")
#
# elif 100 > x > 0:
#     print("pozitiven")
#
# elif x == 0:
#     print("Nula")
#
# elif 0 > x > -100:
#     print("Negativen")
#
# elif -100 >= x >= -999:
#     print("Mnogu negativen")
#
# else:
#     print("Preterano negativen")


# ZADACHA 3
# Да се напише програма што ќе ги генерира оценките врз основа на освоените поени од тестот, според следната табела

# Filip
# poeni = int(input("Vnesete poeni: "))
# if poeni <= 60:
#     print("Ocenka: 1")
# elif poeni>=60 and poeni<=70:
#     print("Ocenka:2")
# elif poeni>=70 and poeni<=80:
#     print("Ocenka: 3")
# elif poeni>=81 and poeni<90:
#     print("Ocenka: 4")
# else:
#     print("Ocenka: 5")

# Aljban
# poeni=int(input())
# if 0<=poeni<=60:
#     print("Ocenka=1")
# elif 60<poeni<=70:
#     print("Ocenka=2")
# elif 70<poeni<=80:
#     print("Ocenka=3")
# elif 80<poeni<=90:
#     print("Ocenka=4")
# else:
#     print("Ocenka=5")

# Stefan
# poeni = int(input())
# if 0 <= poeni <=60:
#     print("1")
# elif 60 < poeni <=70:
#     print("2")
# elif 70 < poeni <=80:
#     print("3")
# elif 80 < poeni <=90:
#     print("4")
# else:
#     print("5")


# poeni = int(input())
# if 0 <= poeni <=60:
#     print("1")
# elif 60 < poeni <=70:
#     print("2")
# elif 70 < poeni <=80:
#     print("3")
# elif 80 < poeni <=90:
#     print("4")
# else:
#     print("5")

# ZADACHA 4
# Да се напише програма што ќе работи како едноставен калкулатор:
# од тастатура ќе чита оператор и два броја и ќе ја изврши наведената операција.

# broj_1 = int(input())
# broj_2 = int(input())
# operator = input()
#
# if operator == "+":
#     print(broj_1+broj_2)
# elif operator == "-":
#     print(broj_1-broj_2)
# elif operator == "*":
#     print(broj_1*broj_2)
# elif operator == "/":
#     print(broj_1/broj_2)
# elif operator == "%":
#     print(broj_1%broj_2)
# elif operator == "//":
#     print(broj_1//broj_2)
# elif operator == "**":
#     print(broj_1**broj_2)
# else:
#     print("Vnesovte nevaliden operator")

# ZADACHA 5
#Напиши програма којашто ќе прочита број на месец од годината и ќе испечати колку денови има овој месец.

# mesec = int(input())
#
# # RESHENIE 1
# if mesec == 1 or mesec == 3 or mesec == 5 or mesec == 7 or mesec == 8 or mesec == 10 or mesec == 12:
#     print("Mesecot ima 31 den")
# elif mesec == 2:
#     print("Mesecot ima 28 ili 29 dena")
# else:
#     print("Mesecot ima 30 dena")
#
# # RESHENIE 2
# if mesec % 2 == 1 and mesec <= 7:
#     print("Mesecot ima 31 den")
# elif mesec % 2 == 0 and mesec > 7:
#     print("Mesecot ima 31 den")
# elif mesec == 2:
#     print("Mesecot ima 28 ili 29 dena")
# else:
#     print("Mesecot ima 30 dena")
#
# # RESHENIE 2.2
# if (mesec % 2 == 1 and mesec <= 7) or (mesec % 2 == 0 and mesec > 7):
#     print("Mesecot ima 31 den")
# elif mesec == 2:
#     print("Mesecot ima 28 ili 29 dena")
# else:
#     print("Mesecot ima 30 dena")

# RESHENIE 3
# meseci_so_31_den = [1, 3, 5, 7, 8, 10, 12]
# if mesec in meseci_so_31_den:
#     print("Mesecot ima 31 den")
# elif mesec == 2:
#     print("Mesecot ima 28 ili 29 dena")
# else:
#     print("Mesecot ima 30 dena")

# ZADACHA 6
# Напиши програма којашто од стандарден влез ќе прочита број на ден од неделата
# и ќе испечати за кој ден станува збор.

# den = int(input())
# if den == 1:
#     print("Ponedelnik")
# elif den == 2:
#     print("Vtornik")
# elif den == 3:
#     print("Sreda")
# elif den == 4:
#     print("Chetvrtok") # itn.

# denovi = {
#     1: "Ponedelnik",
#     2: "Vtornik",
#     3: "Sreda",
#     4: "Chetvrtok",
#     5: "Petok",
#     6: "Sabota",
#     7: "Nedela"
# }
#
# print(denovi.get(den))
# ZADACHA 7
#  Напиши програма во која што ќе се внесе од тастатура име на ученик, оценките по 5 предмети и ќе се пресмета
#  вкупниот збир на оценките, просечна оценка и да се испечати за каков ученик станува збор
#  (одличен, многу добар, добар, доволен, недоволен)

# ime = input()
# matematika = int(input())
# makedonski = int(input())
# geografija = int(input())
# istorija = int(input())
# informatika = int(input())
#
# zbir = matematika + makedonski + geografija + istorija + informatika
# prosek = zbir / 5
#
# print("Ocenka po matematika", matematika)
# print("Ocenka po makedonski", makedonski)
# print("Ocenka po geografija", geografija)
# print("Ocenka po istorija", istorija)
# print("Ocenka po informatika", informatika)
#
# print(f"Zbir na ocenkite: {zbir}, prosek: {prosek}")
# if prosek >= 4.5:
#     print("Uchenikot e odlichen")
# elif prosek >= 3.5:
#     print("Uchenikot e mnogu dobar")
# elif prosek >= 2.5:
#     print("Uchenikot e dobar")
# elif prosek >= 1.5:
#     print("Uchenikot e dovolen")
# else:
#     print("Uchenikot e nedovolen")

# ZADACHA 8
# Да се напише програма што ќе овозможи претворање на броевите во зборови на следниот начин:
# За 89 како излез ќе се добие “osum devet”. Дозволено е да се внесат само двоцифрени броеви.

# Aljban
# x=int(input("x="))
# y=x//10
# z=x%10
# print(y)
# print(z)

# broevi={
#     1:"eden",
#     2:"dva",
#     3:"tri",
#     4:"chetri",
#     5:"pet",
#     6:"shest",
#     7:"sedum",
#     8:"osum",
#     9:"devet"
# }
#
# print("navedeniot broj e", broevi[y],broevi[z])

# Stefan
# broj = {
#     1: "eden",
#     2: "dva",
#     3: "tri",
#     4: "cetiri",
#     5: "pet",
#     6: "shest",
#     7: "sedum",
#     8: "osum",
#     9: "devet",
# }
# x = int(input())
#
# print(broj[x//10])
# print(broj[x%10])

# ZADACHA 12
# Да се напише програма која ќе проверува дали даден карактер е буква, цифра или специјален карактер.

# x = input()
# if x.isdigit():
#     print("Vnesovte cifra")
# elif x.isalpha():
#     print("Vnesovte bukva")
# else:
#     print("Vnesovte karakter")

# ZADACHA 14
# Цените за летовите до одредени градови се дадени во речникот flight_prices. Да се напише програма во која корисникот
# ќе внесе град преку стандарден влез. Доколку имаме цена за летот до тој град да се испечати соодвентата цена
# а доколку нема да се внесе тој град во речникот со цена None и да се испечати соодветна порака дека немаме таква цена.

# flight_prices = {"Dortmund": 4480,
#  "Frankfurt": 7128,
#  "Budapest": 2595,
#  "Berlin": 8910,
#  "Paris": 3537,
#  "Venice": 2668,
#  "London": 2595,
#  "Milan": 2595,
#  "Rome": 5658,
#  "Malta": 5578}
#
# city = input()

# RESHENIE 1
# if city in flight_prices:
#     print(flight_prices[city])
# else:
#     flight_prices[city] = None
#
# print(flight_prices)

# RESHENIE 2
# print(flight_prices.setdefault(city, None))

# ZADACHA 15
# Да се напише програма којашто ќе спојува две листи. Притоа да се внимава на следниве правила:
#
# резултантната листа никогаш да не содржи повеќе од 10 елементи
# резултантната листа никогаш да не содржи помалку од 4 елементи, доколку немаме вкупно 4 елементи
# во двете листи, да се дополни со 0
# резултантната листа не смее да содржи дупликати
# да биде сортирана по азбучен редослед

# list_1 = [1, 2, 3, 4, 5, 6, 9]
# list_2 = [4, 0, 4, 3, 0, 9, 2, 3, 12, 223, 43, 54, 35, 9]
#
# spoena = list_1 + list_2
# spoena = list(set(spoena))
#
# if len(spoena) > 10:
#     spoena = spoena[0:10]
# elif len(spoena) < 4:
#     lista_nuli = [0, 0, 0, 0]
#     # spoena = [1, 2]
#     spoena.extend(lista_nuli)  # spoena [1, 2, 0, 0, 0, 0]
#     spoena = spoena[0:4]  # spoena [1, 2, 0, 0]
#
# sorted(spoena)
# print(spoena)
