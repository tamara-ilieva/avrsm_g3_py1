import math
import random
import numpy as np
import string

# CTRL+SHIFT+ALT+L - оптимизација на imports

# print(math.pi)
# print(math.e)
# math.radians()
# math.degrees()
# math.sin()
# math.log()
# print(math.pow(2, 3))
# print(math.pow(4, 2))
# print(math.sqrt(100))
# math.ceil()
# math.floor()

# import cas4
#
# x = 2
# y = 3
#
# z, r = cas4.zbir_i_razlika(2, 3)
# print(z, r)


# from cas4 import zbir_i_razlika
# x = 4
# y = 5
# print(zbir_i_razlika(4, 5))


#
# mylist = ["python", "java", "c"]
# mylist_2 = [x for x in range(18)]
# random.shuffle(mylist_2)
# print(random.random())

# print(random.choices(mylist, weights=[10, 5, 1], k=14))
# print(random.choices(mylist, cum_weights=[10, 15, 16], k=14))


# Задача 1.0: Компјутерот бира број по случаен избор во ранг 1-100. Корисникот се обидува да го погоди
# случајно избраниот број преку внесување на броеви од стандарден влез се додека не го погоди. Да се изброи колку
# неуспешни обиди има корисникот и да се испечати резултатот (бројот на неуспешни обиди) на екран откако ќе го погоди.

# random_number = random.randint(1, 100)
# print(random_number)
# failed_attempts = 0
# chances = 20
# attempts = np.array([])
#
# while chances > 0:
#     users_guess = int(input())
#
#     if random_number == users_guess:
#         attempts = attempts.astype('int')
#         print(f"Congratulations, you guessed the number! Number of failed attempts: {failed_attempts}.\n\
#          Your attempts: {attempts}")
#         break
#
#     else:
#         if users_guess in attempts:
#             print(f"You already attempted with the number {users_guess}")
#         else:
#             attempts = np.append(attempts, users_guess) # attempts + users_guesss
#             chances -= 1
#             failed_attempts += 1

# Задача 1.1: Да се прошири задачата со тоа што доколку корисникот нема да го погоди бројот во првите 20 обиди,
# програмата ќе заврши. Да се зачувуваат сите обиди на корисникот (во numpy низа) и доколку внесе некој број по втор
# пат да не му се одзема шансата за тоа внесување, дополнително да му се испечати порака "You already attempted with
# the number { num}"


# Задача 2.0:

# names = ["James", "John", "Mark", "Rick", "Taylor", "Ted", "Robin", "Barney", "Joey", "Jessica"]

# Имаме дадена листа од имиња. Од дадената листа да се креира numpy низа. Од низата со помош на random модулот да се
# одбере име по случаен избор. Ова име да му биде прикажано на корисникот којшто ќе може да одбере дали името да се
# зачува во листата или не. Постапката да се повтори k (број внесен на почеток од програмата) пати (или додека не
# снема имиња).

# np_names = np.array(names)
# k = int(input())
#
# m = int(input())
# if m > len(names)/2:
#     print("Please enter a valid number, m must be smaller than len(names)/2.")
#     m = int(input())
#
# protected_names = np.array([])
# for i in range(m):
#     name = input()
#     protected_names = np.append(protected_names, name)
#
#
# for i in range(k):
#     random_name = random.choice(np_names)
#     if random_name in protected_names:
#         continue
#     print(f"Do you want to remove: {random_name}. yes/no")
#     to_remove = input()
#
#     if to_remove == 'yes':
#         index = np.where(np_names == random_name)
#         np_names = np.delete(np_names, index)
#
# print(np_names)

# Задача 2.1: Да му се дозволи на корисникот да „заштити“ одредени имиња од отстранување од листата. Односно да се
# елиминира ситуацијата кадешто за „заштитено“ име ќе биде прашан корисникот дали ќе биде отстрането ова име. На
# почеток корисникот внесува број m којшто означува колку имиња сака да заштити. Овој број не може да биде поголем од
# големината на листата / 2. Доколку се внесе невалиден број да се побара од корисникот повторно да внесе валиден
# број. Откако ќе внесе валиден број, ги внесува m-те заштитени имиња.


# Задача 3:
# Да се напише функција којашто ќе генерира пасворд. Пасвордот треба да ги исполнува следниве услови:
# - барeм две големи букви
# - барем една мала буква
# - барем 1 цифра
# - барем 1 карактер

# Hint, check the output:
# letters = list(string.ascii_letters)
# lowercase_letters = list(string.ascii_lowercase)
# uppercase_letters = (list(string.ascii_uppercase))
#
# first_uppercase_letter = random.choice(uppercase_letters)
# second_uppercase_letter = random.choice(uppercase_letters)
#
# lowercase_letter = random.choice(lowercase_letters)
#
# digits = [x for x in range(10)] # lista od site cifri
# random_digit = str(random.choice(digits))
#
# characters = ['!', '@', '#', '$', '%', '^', '&']
# random_character = random.choice(characters)
#
# password_list = [first_uppercase_letter, second_uppercase_letter, lowercase_letter, random_character, random_digit]
# print(password_list)
# full_dataset = letters + digits + characters
# for i in range(5):
#     password_list.append(random.choice(full_dataset))
#
# random.shuffle(password_list)
# print(password_list)
# password_str = ''
#
# for i in password_list:
#     password_str = password_str + str(i)
#     # print(password_str)
#
# print(password_str)

# Daniel

# import random
# import numpy as np
#
# names = ["James", "John", "Mark", "Rick", "Taylor", "Ted", "Robin", "Barney", "Joey", "Jessica"]
# np_names = np.array(names)
# k = int(input("Vesete broj kolku iminja da se otstranat: "))
# protected_names = np.array([])
# prottected_names_number = int(input("Vnesete broj na zastiteni iminja: "))
#
# while True:
#     if prottected_names_number > (len(np_names) / 2):
#         prottected_names_number = int(input("Vnesete broj na zastiteni iminja: "))
#         continue
#     else:
#         for i in range(prottected_names_number):
#             name = input("Vnesete ime: ")
#             protected_names = np.append(protected_names, name)
#         break
#
# print(protected_names)
#
# for i in range(k):
#     random_name = random.choice(np_names)
#     print(f"Do you want to remove: {random_name}. yes/no")
#     to_remove = input()
#
#     if to_remove == 'yes':
#         if random_name in protected_names:
#             print(f"This {random_name} is protected.")
#             continue
#         else:
#             index = np.where(np_names == random_name)
#             np_names = np.delete(np_names, index)
#
# print(np_names)
