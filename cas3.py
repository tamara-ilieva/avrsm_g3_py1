# Задача 1
# Напиши програма која ќе прочита
# три броеви (a,b,c) и провери колку
# броеви помеѓу а и b се деливи со c.

# a = int(input())
# b = int(input())
# c = int(input())
# counter = 0
#
# for number in range(a, b+1):
#     if number % c == 0:
#         counter += 1
# else:
#     print(counter)


# Задача 2
# Напиши програма која ќе пресмета
# факториел за даден број
# 5! = 5 * 4 * 3 * 2 * 1

# n = int(input())
# faktoriel = 1
# for i in range(1, n+1):
#     faktoriel *= i
# else:
#     print(faktoriel)


# Задача 3
# Напиши програма која ќе ги
# испечати сите прости броеви од 1 до
# n, кадешто n е број кој што се внесува
# преку стандарден влез.

# n = int(input())
# counter_prime_numbers = 0
#
# for number in range(1, n + 1):
#     for delitel in range(2, number):
#         if number % delitel == 0: # ne e prost, dava ostatok 0 - deliv so delitel
#             break
#     else:
#         counter_prime_numbers += 1
# else:
#     print(counter_prime_numbers+1)

# Задача 4
# Да се испечи следната шема за
# броеви од 1 до n, n е број којшто се
# внесува од тастатура

# n=5
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# n = int(input())
# for i in range(1, n+1): # 1 2 3 4 5
#     for j in range(1, i+1):
#         print(f"{j} ", end="")
#     print("\n", end="")  # print()


# Задача 5
# Да се внесе број од тастатура и да
# се испечати неговата „превртена“
# верзија

# 12345 -> 54321
# 5, 12345%10
# * 10  + 5

# number = int(input())
#
# reversed_number_string_solution = str(number)[::-1] # solution 1
#
# reversed_number = 0
# number_str = str(number)
# reversed_number_str = ''
#
# for i in range(len(number_str)-1, -1, -1):
#     # print(i, number_str[i])
#     reversed_number_str += number_str[i]
#
# print(int(reversed_number_str)) # solution 2


# while number != 0:  # dodeka ima cifri izvrshuvaj go ciklusot
#     digit = number % 10  # poslednata cifra od number
#     reversed_number = reversed_number * 10 + digit  # 5, 54, 543 ....
#     number = number // 10
#
# print(reversed_number) # solution 3

# Задача 6
# Да се напише програма која ќе ги
# најде сите броеви од m до n
# (броеви коишто се внесуваат од
# тастатура) кадешто секоја цифра
# во бројот е парен број. Да се
# изброи бројот на вакви броеви и
# резултатот да се испечати на
# екран

# m = int(input())
# n = int(input())
# counter = 0
#
# for number in range(m, n+1):
#     number_copy = number
#     while number != 0:
#         digit = number % 10
#         if digit % 2 != 0:
#             break
#         number //= 10
#     else:
#         print(number_copy)
#         counter += 1
# print("Brojot na vakvi broevi e: ", counter)


# Задача 7
# Да се напише програма којашто ќе ја
# пресмета возраста на кучето од кучешки
# години во човечки години.
# Првите 2 години, кучешките години се
# еднакви на 10.5 човечки години. Потоа,
# секоја кучешка година е еднаква на 4
# човечки години.

# Stefan
# age = int(input())
# dog_age = 0
# for i in range(age):
#     if i < 2:  # 0, 1
#         dog_age += 10.5
#     else:
#         dog_age += 4
# print(dog_age)

# Daniel
# dog_years = int(input())
# year = 1
# human_years = 0
# while year <= dog_years:
#     if year == 1 or year == 2:
#         human_years += 10.5
#     else:
#         human_years += 4
#     year += 1
# else:
#     print(f"The dog has {int(human_years)} human years.")

# Alban
# x=int(input("x="))
# if x < 2:
#     y=(x/2)*10.5
# else:
#     y=4*(x-2)+(2*10.5)
# print("Vrednosta na kuceshkite godini vo covecki godini e:",y)

# Filip
# age = int(input())
# human_age = 0
# for i in range(age):
#     if i < 2:
#         human_age += 10.5
#     else:
#         human_age += 4
# print(human_age)

# Задача 8
# Да се напише програма којашто ќе ги испринта
# сите броеви од 1 до n (n е број внесен од
# тастатура). Доколку бројот се дели со 3 да се
# испечати "#Tri" наместо бројот, доколку се дели
# со 5 да се испечати "#Pet" а доколку се дели и
# со 3 и со 5 да се испечати "#TriPet" наместо
# бројот

# n = int(input())
# for i in range(1, n+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("#TriPet")
#     elif i % 3 == 0:
#         print("#Tri")
#     elif i % 5 == 0:
#         print("#Pet")
#     else:
#         print(i)


# Задача 9
# Да се испечатат сите стрингови од
# една листа како lowercase линии.

# lines = ["aBcccbB", "Ova e linija 2.", "Ova e TreTa linija."]
# for i in lines:
#     print(i.lower())

# Задача 10
# Да се напише програма која прима
# некој стринг на влез и ќе изброи
# колку букви и броеви се внесени.

# str_example = " srijegoj 3995 4wej geriog%%78342!@ !! 94"
# counter_letters = 0
# counter_digits = 0
#
# for character in str_example:
#     if character.isdigit() is True:
#         counter_digits += 1
#     elif character.isalpha() is True:
#         counter_letters += 1
# else:
#     print(f"Letters: {counter_letters}, digits: {counter_digits}")


# Задача 11
# Напиши програма којашто ќе ја
# испечати таблицата за множење
# за бројот којшто ќе се внесе од
# тастатура

# n = int(input())
# for i in range(1, 11):
#     print(f"{i} * {n} = {i*n}")

# Задача 12
# Да се напише програма којашто го
# принта квадратот на сите броеви
# од 1 до 20

# for i in range(1, 21):
#     print(i*i)

# Задача 13
# Да се напише програма којашто ќе
# прими стринг како влез од
# корисникот и ќе ги испринта
# карактерите коишто се наоѓаат на
# напарни позиции во стрингот

# Задача 13.1
# Да се дополни претходната задача
# такашто ќе направи и уште еден
# стринг од карактерите на парните
# позиции

# Filip
# n = input()
# par = ""
# for i in range(len(n)):
#     if i % 2 != 0:
#         print(n[i])
#     else:
#         par += n[i]
# print(par)

# Daniel
# text = input()
# new_text = ''
#
# for i in range(len(text)):
#     if i % 2 == 0:
#         print(text[i])
#     else:
#         new_text += text[i]
# print(new_text)

# Andrej
# input_text = input()
# new_string = ""
# for i in input_text[1::2]:
#     print(i)
#
# for i in input_text[::2]:
#     new_string += i
# print(new_string)


# Задача 14
# Да се напише програма којашто ќе
# испечати на екран колку пати даден
# збор се содржи во една реченица.
# Пример:
# Ivan ima 25 godini. Ivan raboti kako
# Python Developer. Programiranje so Python
# ima naucheno na kurs vo Semos edukacija.
# Ivan mnogu si ja saka rabotata.

# example = "Ivan ima 25 godini. Ivan raboti kako Python Developer. Programiranje so Python ima naucheno na kurs vo " \
#           "Semos edukacija. Ivan mnogu si ja saka rabotata. "

# Задача 15
# Напиши програма којашто ќе ја
# печати низата на Фибоначи до nтиот елемент. n е број којшто се
# внесува од страна на корисникот.
# 0, 1, 1, 2, 3, 5, 8, 13, 21...

# fibonachi = [0, 1]
# n = int(input())
# for i in range(1, n-1):
#     fibonachi.append(fibonachi[i]+fibonachi[i-1])
# print(fibonachi)

# Задача 16
# Напиши програма којашто ќе
# изброи колку цифри има даден
# број


# Задача 17
# Да се напише програма за
# пресметување на y=xⁿ за даден
# природен број n и реален број x


# Задача 18
# Да се напише програма која ќе проверува
# дали некој кандидат е одбран или не врз
# основа на неговата возраст и висина, при
# што се одбираат кандидати постари од 15
# години и минимална висина од 140 cm. На
# крај да се испринта колку од внесените
# кандидати го исполнуваат условот.
# Податоците за кандидатите ги имате во
# дадената листа од речници.

# candidates = [
#     {"name": "Biljana", "age": 13, "height": "145"},
#     {"name": "Tamara", "age": 19, "height": "156"},
#     {"name": "Sandra", "age": 16, "height": "138"},
#     {"name": "Marko", "age": 18, "height": "160"},
#     {"name": "Sandra", "age": 16, "height": "178"},
#     {"name": "Aleks", "age": 10, "height": "128"},
#     {"name": "Angela", "age": 19, "height": "180"},
#     {"name": "Kristijan", "age": 17, "height": "170"},
#     {"name": "Nikola", "age": 19, "height": "165"},
# ]

# Задача 19
# Да се напише програма која ќе го
# пресметува збирот на цифрите за даден
# број.
# Пример:
# 4526 = 17

# Задача 20
# Благ број е број што е составен само од
# парни цифри (0, 2, 4, 6, 8). Во зададен
# опсег (почетокот m и крајот на опегот n се
# цели броеви чија вредност се внесува од
# тастатура), да се најде и испечати
# најмалиот „благ број“
# . Ако не постои таков
# број, да се испечати NE.

# m = int(input())
# n = int(input())

# 20 21 22 23 24 25 26 27 28
#  20 22 24 26 28

# 13 24 20

# for number in range(m, n):
#     number_copy = number
#
#     while number != 0:
#         digit = number % 10
#         if digit % 2 != 0:  # ako najde barem edna neparna cifra, togash brojot ne e "blag broj"
#             break
#         number //= 10
#     else:
#         print(number_copy)
#         brojot_e_najden = True
#         break
# else:
#     print("Nema takov broj")


# Задача 21 - ZA DOMA!!
# Eден природен e „интересен“ ако неговиот
# обратен број е делив со неговиот број на
# цифри. Обратен број е бројот составен од
# истите цифри, но во обратен редослед (на
# пример, 653 е обратен број на бројот 356).
# Од тастатура се внесува природен број n (
# n > 9). Да се најде и отпечати најголемиот
# природен број помал од n кој што е
# „интересен“
# . Ако внесениот број не е
# валиден, да се отпечати соодветна порака
# (Brojot ne e validen)

# Задача 22
# Од стандарден влез се чита еден
# природен број n. Меѓу природните броеви
# помали од n, да се најде оној чиј што збир
# на делителите е најголем. Во
# пресметувањето на збирот на делителите
# на даден број, да не се зема предвид
# самиот број.


# Задача 23
# Да се напише програма во која од стандарден влез
# прво се внесува еден позитивен цел број z, а потоа
# последователно се внесуваат парови цели броеви
# (a, b). Внесувањето на парови цели броеви треба
# да заврши кога корисникот ќе го внесе парот (0, 0).
# Треба да се пресмета колку пати z е еднаков на
# збирот на секој внесен пар броеви a и b, како и
# колкав процент од вкупниот број внесени парови
# (a, b) даваат збир z (ЗАБЕЛЕШКА: парот (0, 0) не се
# зема во предвид при извршувањето на
# пресметките!)


# Задача 24
# Од стандарден влез се читаат знаци се додека не
# се прочита извичник. Во вака внесениот текст се
# скриени цели броеви (помали од 100). Да се
# напише програма што ќе ги прочита сите знаци и
# на излез ќе го испечати збирот на сите броеви
# скриени во текстот.

#

# def panagram(text, alphabet):
#     set_text = set(text.lower())
#     set_text.remove(" ")
#     if set_text == alphabet:
#         return True
#     return False
#
#
# alphabet = {
#     'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
#     'v', 'b',
#     'n', 'm'}
#
# text = "The quick brown fox jumps over the lazy dog"
# res = panagram(text, alphabet)

