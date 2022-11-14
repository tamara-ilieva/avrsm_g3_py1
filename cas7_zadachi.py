# EXERCISE 1:
# Below, we have provided buggy code. Add a try/except clause so the code runs without errors. If a blog post didn’t
# get any likes, a ‘Likes’ key should be added to that dictionary with a value of 0.

# blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
#               {'Likes': 13, 'Comments': 2, 'Shares': 1},
#               {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
#               {'Comments': 4, 'Shares': 2},  # somnitelen
#               {'Photos': 8, 'Comments': 1, 'Shares': 1},  # somnitelen
#               {'Photos': 3, 'Likes': 19, 'Comments': 3}]
#
# total_likes = 0
# total_shares = 0
#
# for post in blog_posts:
#     try:
#         total_likes = total_likes + post['Likes']  # 0, 21, 21+13, 21+13+33, 21+13+33
#         total_shares = total_shares + post['Shares']
#     except KeyError as message:  # greshka koga ne postoi kluchot vo rechnikot -> 'Likes' vo post
#         post['Likes'] = 0
#         print(message)
#
# print(blog_posts)
#
#
# def fun(a, b):
#     if a < 5:
#         raise ValueError('Please enter a number bigger than 5')
#     return a + b
#
#
# a = int(input())
# b = int(input())
#
# try:
#     fun(a, b)
#
# except ValueError as e:
#     print(e)
#
#
# # Da se kreiraat 4 funckii za presmetka na matematichkite operacii (-, +, *, /)
# # Operaciite se izvrshuvaat na dva broja, se vnesuvaat od standarden vlez (input())
# # Da se sprechi delenje so 0
# # Da se sprechi vnes na znaci ili bukvi
# # Da se sprechi negativen rezultat pri odzemanje
# # Uslovite da se implementiraat preku handleing na iskluchoci (exceptions)
#
#
# # Dimitar
# def zbir(x, y):
#     return x + y
#
#
# def razlika(x, y):
#     return x - y
#
#
# def proizvod(x, y):
#     return x * y
#
#
# def kolichnik(x, y):
#     return x // y
#
#
# broj1 = int(input("Vnesi prv broj:"))
# broj2 = int(input("Vnesi vtor broj:"))
#
# try:
#     print(broj1, "/", broj2, "=", kolichnik(broj1, broj2))
# except ZeroDivisionError:
#     print("Cannot divide with 0")
#
# print(broj1, "+", broj2, "=", zbir(broj1, broj2))
# print(broj1, "-", broj2, "=", razlika(broj1, broj2))
# print(broj1, "*", broj2, "=", proizvod(broj1, broj2))
#
#
# # Daniel
# def subtract(prv, vtor):
#     if vtor > prv:
#         raise ValueError("Rezultatot e negativen broj.")
#     return prv - vtor
#
#
# def divide(prv, vtor):
#     if vtor == 0:
#         raise ZeroDivisionError("Ne moze da se deli so 0.")
#     return prv / vtor
#
#
# a = input()
# b = input()
#
# try:
#     subtract(int(a), int(b))
#     divide(int(a), int(b))
# except ValueError as error:
#     print(error)
# except ZeroDivisionError as error:
#     print(error)
#
#
# # Nikolina
# def odzemanje():
#     a = 5
#     b = 8
#     resultat = a - b
#     if resultat < 0:
#         raise Exception("no negative resultat")
#     return resultat
#
#
# try:
#     odzemanje()
# except Exception as e:
#     print(e)
#
#
# # Stefan
# def sobiranje(a, b):
#     return a + b
#
#
# def odzemanje(a, b):
#     return a - b
#
#
# def mnozenje(a, b):
#     return a * b
#
#
# def delenje(a, b):
#     return a / b
#
#
# try:
#     a = int(input())
#     b = int(input())
#
# except ValueError as e:
#     print("Vrednostite moraat da bidat numericki")
#
# try:
#     delenje(a, b)
# except ZeroDivisionError:
#     print("Ne moze da se deli so 0")
# else:
#     print(delenje(a, b))
#
#
# # Andrej
# def addition(a, b):
#     try:
#         return a + b
#     except TypeError as e:
#         print(e)
#
#
# def subtraction(a, b):
#     if a - b < 0:
#         raise ValueError("Negative result while subtracting")
#     else:
#         try:
#             return a - b
#         except TypeError as e:
#             print(e)
#
#
# def multiplication(a, b):
#     try:
#         return a * b
#     except TypeError as e:
#         print(e)
#
#
# def division(a, b):
#     try:
#         return a / b
#     except TypeError as e:
#         print(e)
#     except ZeroDivisionError as e:
#         print(e)
#
#
# num_a = int(input("Input a: "))
# operation = input("Input math operation (-, +, *, /): ")
# num_b = int(input("Input b: "))
#
# if operation == "+":
#     add = addition(num_a, num_b)
#     print(add)
#
# if operation == "-":
#     try:
#         subtract = subtraction(num_a, num_b)
#         print(subtract)
#     except ValueError as e:
#         print(e)
#
# if operation == "*":
#     multiply = multiplication(num_a, num_b)
#     print(multiply)
#
# if operation == "/":
#     divide = division(num_a, num_b)
#     print(divide)
#
#
# # Elena S
# def zbir(a, b):
#     zbir = a + b
#     print(zbir)
#     return zbir
#
#
# def odz(a, b):
#     odz = a - b
#     return odz
#
#
# def mn(a, b):
#     mn = a * b
#     return mn
#
#
# def delenje(a, b):
#     try:
#         delenje = a // b
#     except ZeroDivisionError as e:
#         print(e)
#     else:
#         return delenje
#
#
# a = int(input())
# b = int(input())

# The code below assigns the 5th letter of each word in food to the new list fifth. However, the code currently
# produces errors. Insert a try/except clause that will allow the code to run and produce of list of the 5th letter
# in each word. If the word is not long enough, it should not print anything out.

# EXERCISE 2
food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []

for x in food:
    try:
        fifth.append(x[4])
    except IndexError:
        pass

print(fifth)