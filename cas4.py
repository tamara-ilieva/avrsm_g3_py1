# HOMEWORK 1

# ---------------------------------------------------------
# Напиши програма којашто ќе земе string од стандарден влез. Направи ги следните модификации и операции со овој стринг:
# text = input()
# Да се отстранат празните места на почеток и крај од стрингот
# text = text.strip()

# Да се изброи колку пати се појавува буквата „а“
# а колку буквата „м“ во стрингот
# (да се земат во предвид и големите и малите букви при ова броење)

# text = text.lower()
# counter_a = text.count('a')
# counter_m = text.count('m')

# lowercase_text_version = text.lower()  # lowercase verzija od stringot
#
#
# counter_a = text.count('a')  # mali a
# counter_A = text.count('A')  # golemi A
# counter_a = counter_A + counter_a
#
# counter_a_2 = text.count('a') + text.count('A')
#
# counter_m = text.count('m')  # mali a
# counter_M = text.count('M')  # golemi A
# counter_m = counter_M + counter_m
#
# counter_m_2 = text.count('m') + text.count('M')
#


# Да се испечати бројот на појавувања соодветно за двете букви

# print(counter_a_2, counter_m_2)

# Да се замени буквата „т“ во стрингот со карактерот „$“
# а буквата „б“ со карактерот „*“
# (да се земат во предвид и големи и малите букви при оваа модификација)

# text = text.replace('t', '$').replace('b', '*').upper().lower()
# print(text)

# Да се изброи колку цифри содржи стрингот и да се испечати резултатот
# python 123 python -> 3

# counter_digits = [text.count('0'), text.count('1'), text.count('2'), text.count('3'), text.count('4'), text.count(
# '5'), text.count('6'), text.count('7'), text.count('8'), text.count('9')] print(counter_digits) sum_digits = sum(
# counter_digits) print(sum_digits)

# Напиши програма во којашто корисникот ќе внесе 5 имиња од тастатура. Ја имате даденава листа од имиња во програмата.
# names = ["teodora", "aleksandar", "jovana"]

# Додај ги имињата внесени од корисникот во листата names
# names.append(input())
# names.append(input())
# names.append(input())
# names.append(input())
# names.append(input())
#
# print(names)

# Сортирај ја листата по обратен азбучен редослед (z-a)

# names.sort(reverse=True)

# names.sort()
# names.reverse()

# names.sort()
# names = names[::-1]

# print(names)

# Направи уште една листа (names_copy) којашто ќе претставува копија од листата names
# names_copy = names.copy()

# Избриши ги сите елементи од листата names, за наредните барања користи ја листата names_copy
# names.clear()

# Креирај уште една листа names_2 = [“daniela”, “ana”,”ivan”, “boris”, “aleksandar”]

# names_2 = ["daniela", "ana", "ivan", "boris", "aleksandar"]


# Додај ги елементите од листата names_2 во names_copy
# names_copy.extend(names_2)

# Отстрани го името „ana“ од листата
# names_copy.remove("ana")
# print(names_copy)


# Отстрани ги дупликатите од листата

# names_copy = list(set(names_copy))
# print(names_copy)
# -----------------------------------------------------------------------------------


# dictionary = {"name": "Tamara",
#               "age": 24,
#               "course": "Python"}
#
# print(dictionary.items())
# print(dictionary.keys())
# print(dictionary.values())
#
# for i in dictionary.keys():
#     print(f"Key: {i}")
#
# for i in dictionary.values():
#     print(f"Values: {i}")
#
# for key, value in dictionary.items():
#     print(f"{key} - {value}")


# ------------------------------------------------------------------
# def my_function(name, last_name=""):
#     """
#         Combines the first and last name of an user into a full name string
#
#     :param name: user's first name
#     :type: str
#     :param last_name: user's last name
#     :type: str
#     :return: full_name
#     """
#
#     return name + " " + last_name
#
#
# full_name = my_function("tamara")
# print(full_name)
# -------------------------------------------------------------------


# -------------------------------------------------------------------

# == Да се напише функција којашто ќе пресметува збир на броеви во една листа

# def sum_numbers_in_list(list_of_numbers):
#     """
#         Sums all numbers in the list given as an argument
#     :param list_of_numbers: list of numbers for which we want to calculate the sum
#     :type: list
#     :return: sum of the numbers
#     """
#     # return sum(list_of_numbers)
#
#     suma = 0
#     for i in list_of_numbers:
#         suma += i
#     return suma
#
#
# res = sum_numbers_in_list([1, 2, 3, 1])
# print(res)


# == Да се напише функција која ќе наоѓа максимум од три броја

# def max_of_three(b1, b2, b3):
#     """
#         Finds the maximum of the three numbers
#     :param b1: first number
#     :type: int
#     :param b2: second number
#     :type: int
#     :param b3: third number
#     :type: int
#     :return: maximum of the three numbers
#     """
#
#     if b1 > b2:
#         if b1 > b3:
#             return b1
#         else:
#             return b3
#     elif b2 > b3:
#         return b2
#     else:
#         return b3
#
#
# res = max_of_three(1, 2, 3)
# print(res)

# == Да се напише функција којашто ќе пресметува факториел на даден број
# бројот треба да се внесе од страна на корисникот
# n! = n * n-1 * n-2 * ... * 1
# 5! = 5 * 4 * 3 * 2 * 1

# Filip
# def factoriel(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factoriel(n - 1)
#
#
# print(factoriel(5))
#
#
# # Dimitar
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# n = int(input("Input a number to compute the factiorial : "))
# print(factorial(n))
#
#
# # Stefan
#
# def faktoriel(x):
#     f = 1
#     while x > 0:
#         f *= x
#         x -= 1
#     return f
#
#
# n = int(input())
# print(faktoriel(n))
#
# # Bojan
# broj = int(input("Vnesi broj", ))
#
#
# def faktoriel(broj):
#     if broj < 2:
#         return 1
#     else:
#         return broj * faktoriel(broj - 1)
#
#
# print(faktoriel(broj))


# == Да се напише функција којашто ќе враќа листа од сите троцифрени броеви коишто се деливи со сумата од нивните цифри
# 100 -> 1 + 0 + 0 = 1,  100%1 == 0?

# Stefan
# def funkcija():
#     l = []
#     for i in range(100, 1000):
#         pom = i
#         sum = 0
#         while pom > 0:
#             sum += pom % 10
#             pom //= 10
#         else:
#             if i % sum == 0:
#                 l.append(i)
#     return l
#
#
# print(funkcija())
#
# # Nachin so 2 funkcii
#
# def suma_od_cifri(n):
#     sum = 0
#     while n > 0:
#         sum += n % 10
#         n //= 10
#     return sum
#
#
def funkcija_2():
    l = []
    for i in range(100, 1000):
        suma = suma_od_cifri(i)
        if i % suma == 0:
            l.append(i)

    return l

#Filip
def function_numbers():
    list_of_numbers = []
    for i in range(100, 1000):
        y = i
        number_1 = int(y % 10)
        y = y / 10
        number_2 = int(y % 10)
        y = y / 10
        number_3 = int(y % 10)

        if i % int(number_3 + number_2 + number_1) == 0:
            list_of_numbers.append(int(i))
    print(list_of_numbers)


function_numbers()

# == Да се напише функција којашто ќе наоѓа НЗД на 2 броја коишто се внесени од страна на корисникот преку тастатура

# ==  Да се напише функција show_employee() којашто ќе ги прима како аргументи името и платата на вработениот и ќе ги
# прикаже на екран. Доколку немаме внесено плата за вработениот да се додели стандардна вредност 9000.

def show_employee(last_name, name="No name", salary=9000):
    print(f"Name of employee: {name}-{last_name}, salary: {salary}")


show_employee(salary=10000, name="Ana", last_name="Angelova")
show_employee("Tamara")

# == Да се напише функција којашто ќе прими 2 броја и ќе ги пресмета збирот и разликата. Од функцијата да се вратат
# двете вредности.

def zbir_i_razlika(a, b):
    zbir = a + b
    razlika = a - b

    return zbir, razlika
    # return [zbir, razlika]
    # return {"zbir": zbir, "razlika": razlika}


# res = zbir_i_razlika(5, 2)
# z, r = zbir_i_razlika(5, 2)
# print(z, r)


# a = 1
#
# def f():
#     print('Inside f() : ', a)
#
# def g():
#     a = 2
#     print('Inside g() : ', a)
#
# def h():
#     global a
#     a = 3
#     print('Inside h() : ', a)

# print('global : ', a)
# f()
# print('global : ', a)
# g()
# print('global : ', a)
# h()
# print('global : ', a)
