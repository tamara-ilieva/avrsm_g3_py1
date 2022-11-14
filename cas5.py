# Да се напише lambda функција којашто ќе го наоѓа степенот на одреден број. (x^y)

# # Bojan
# x = lambda a, b: a ** b
#
#
# # Daniel
# def pow_function(n):
#     return lambda a: a ** n
#
#
# x = int(input("Vnesete x: "))
# y = int(input("Vnesete y: "))
#
# power = pow_function(y)
# print(power(x))
#
#
# # Andrej
# def power_of_num(x):
#     return lambda y: print(f"the power of {x}^{y} is: ", x ** y)
#
#
# x = power_of_num(2)
# x(3)
#
#
# # Stefan
# def func(n):
#     return lambda a: a ** n
#
#
# x = func(3)
# print(x(2))

# Со помош на lambda функција да се сортира листата од торки
#
# students = [
#     ("Tea", 100),
#     ("Ana", 12),
#     ("Marija", 56),
#     ("Aleksandar", 92),
#     ("Milan", 78),
#     ("Ivan", 45)
# ]
#
# students.sort(key=lambda x: x[1], reverse=True)
#
#
# # Да се извадат посебно положените а посебно неположените студенти. Услов за положување е над 50 поени.
#
# polozheni = [student for student in students if student[1] >= 50]
# nepolozheni = [student for student in students if student[1] < 50]
#
# # Да се креира листа само со имињата од положените студенти и да се сортираат по азбучен редослед
# iminja_polozheni = [student[0] for student in polozheni]
# iminja_polozheni.sort()
#
# # Да им се додадат плус 5 поени на неположените студенти поради грешка на професорите при преглед на задачите и
# # повторно да се извршат пресметките
#
# new_students = [student if student[1] >= 50 else (student[0], student[1] + 5) for student in students]
# new_polozheni = [student for student in new_students if student[1] >= 50]
# new_nepolozheni = [student for student in new_students if student[1] < 50]
#
# new_iminja_polozheni = [student[0] for student in new_polozheni]
# new_iminja_polozheni.sort()
#
#
# # Да се пресмета процентот на положеност пред и по додавање на дополнителните поени
# procent_polozhenost = (100/len(students) * len(polozheni))
# new_procent_polozhenost = (100/len(students) * len(new_polozheni))


# Имаме листа којашто содржи информации за вработените во една фирма - нивното име и износ на плата

employees = [
    ("Tea", 87000),
    ("Ana", 12300),
    ("Marija", 56000),
    ("Aleksandar", 92000),
    ("Milan", 7800),
    ("Ivan", 34000),
    ("Ivana", 13450)
]

# Фирмата одлучила да им се даде покачување на вработените за 6% од нивната моментална плата, изврши ја промената во
# листата

# Andrej

# salary_raise = [salary[1] + (salary[1] * 0.06) for salary in employees]
# print(salary_raise)

employees = [(e[0], e[1] + (e[1] * 0.06)) for e in employees]
print(employees)

# Владата одлучува да се зголеми минималната плата на 18000, имплементирај ја промената во листата

# Alban
employees = [e if e[1] > 18000 else (e[0], 18000) for e in employees]
print(employees)

# Daniel
employees = [(e[0], e[1] if e[1] >= 18000 else 18000) for e in employees]
print(employees)

# Stefan
employees = [(x[0], x[1] if x[1] > 18000 else 18000.0) for x in employees]
print(employees)

# Фирмата одлучува да ги награди Ивана и Милан со дополнително зголемување од 10000

# Alban
employees = [(e[0], e[1] + 10000) if e[0] == "Ivana" or e[0] == "Milan" else (e[0], e[1]) for e in employees]
print(employees)

# # Daniel
# employees = [(e[0], e[1] + 10000 if e[0] == "Milan" or e[0] == "Ivana" else e[1]) for e in employees]
# print(employees)
#
# # Bojan
# employees = [e if (e[0]!="Ivana" and e[0]!="Milan") else (e[0],e[1]+10000) for e in employees]
# print(employees)
#
# # Andrej
# employees = [(e[0], e[1] if e[0] != "Milan" and e[0] != "Ivana" else e[1] + 10000) for e in employees]
# print(employees)
#
# # Dimitar
# employees = [(x[0], x[1] + 10000 if x[0] == 'Ivana' or x[0] == 'Milan' else x[1]) for x in employees]
# print(employees)
#
# # Stefan
# employees = [(x if x[0] != 'Ivana' else (x[0], x[1] + 10000.0)) for x in employees]
# print(employees)


# Фирмата одлучува да ја отпушти Ана

# Filip
employees = [e for e in employees if e[0] != "Ana"]
print(employees)

# Stefan
employees = [x for x in employees if x[0] != "Ana"]
print(employees)

# Daniel
for e in employees:
    if e[0] == "Ana":
        employees.pop(employees.index(e))


# Фирмата одлучува да им се намали платата за 10% на сите што земаат над 50000 поради економска криза

# Filip
employees = [e if e[1] < 50000 else (e[0], e[1] - (e[1] * 0.10)) for e in employees]

# Daniel
employees = [(e[0], e[1] if e[1] <= 50000 else e[1] - e[1] * 0.1) for e in employees]
print(employees)


# Да се сортира листата според износот на плата
employees.sort(key=lambda x: x[1])
print(employees)

# Да се одвојат првата половина (помалку платени) и втората половина (повеќе платени) од листата во посебни листи

half = len(employees)/2
print(half)
employees_less_paid = employees[:int(half)]
employees_more_paid = employees[int(half):]
print(employees_less_paid)
print(employees_more_paid)



candidates = [
    ("Marija", 159, 58, 21, 1, 'female', "Atanasova"),
    ("Veronika", 170, 65, 17, 3, 'female', "Gjorgjieva"),
    ("Martina", 167, 70, 29, 8, 'female', "Mileva"),
    ("Antonio", 186, 89, 24, 6, 'male', "Atanasov"),
    ("Marko", 179, 62, 28, 5, 'male', "Mitrov"),
    ("Ilija", 190, 98, 32, 12, 'male', "Petreski"),
    ("Monika", 155, 50, 16, 3, 'female', "Spasova")
]

