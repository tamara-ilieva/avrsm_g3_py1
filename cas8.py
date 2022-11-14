# f = open("primer1.txt", "a")
#
# for i in range(10):
#     f.write(str(i))
#
# f.close()

# sodrzhina = f.read()
# print(sodrzhina)

#print(f.read(5))

# line1 = f.readline()
# line2 = f.readline()
# print(line1)
# print(line2)

# for line in f:
#     print(line)

# try:
#     f = open('primer11.txt', 'x')
# except FileExistsError as e:
#     print(e)

# 1 - пресметај аритметичка средина на броевите од фајлот primer1.txt и додади го резултатот на крај од фајлот
# f = open("primer1.txt", "r")
# lista = []
#
# for num in f:
#     num_new = num.replace("\n", "")
#     num_new = int(num_new)
#     lista.append(num_new)
#
# f.close()
#
# f = open("primer1.txt", "a")
# zbir = 0
# for i in lista:
#     zbir+=i
# aritmetichka_sredina = zbir/len(lista)
# f.write(f"\n Average: {aritmetichka_sredina}")
#
# f.close()

# 2. Да се ископира содржината од фајлот primer во нов фајл
# f = open("primer.txt", "r")
# f2 = open("copy_primer.txt", "w")
# f2.write(f.read())
# f.close()
# f2.close()

# 3. Да се подредат сите броеви од фајлот primer3 и да се запишат во нов фајл

# f = open("primer3.txt", "r")
# lista = []
# for i in f:
#     num = i.replace("\n", "")
#     lista.append(int(num))
#
# lista.sort()
# f2 = open("sortirani_primer3.txt", "w")
# for i in lista:
#     f2.write(f"{str(i)}\n")
#
# f.close()
# f2.close()

# 4. Да се сортираат имињата од фајлот zadacha4.txt во самиот фајл

# Daniel
# f = open("zadacha4.txt")
# names = []
#
# for name in f:
#     names.append(name)
# f.close()
#
# names.sort()
#
# f2 = open("zadacha4_copy.txt", 'w')
# for name in names:
#     f2.write(name)
# f2.close()
#
# # Andrej
# f = open("zadacha4.txt")
# content = f.readlines()
# content.sort()
# f.close()
#
# f_2 = open("zadacha4.txt", "w")
# f_2.writelines(content)
# f_2.close()

# f = open("zadacha4.txt")
# linii = f.readlines() # kreira lista od stringovi, sekoj red od fajlot e poseben element vo listata
# print(linii)
#
# f2 = open("zadacha41.txt", "w")
# f2.writelines(linii)
# f.close()
# f2.close()

# Filip

# f = open('zadacha4.txt', 'r+')
# lista = []
# for i in f:
#     name = i.replace("\n","")
#     lista.append(name)
#
# lista.sort()
# for i in lista:
#     f.write(f'{str(i)}\n')

# f = open("zadacha4_1.txt", "r+")
# iminja = f.readlines()
# iminja.sort()
# f.writelines(iminja)
# f.close()

# f = open("C://Users//Steets//Desktop//test_desktop.txt") # otvaranje na fajlovi so celosna pateka
# print(f.read())

# f = open("files/file1.txt")
# print(f.read())





# 5.
# Да се напише програма која на корисникот ќе му
# дозволи да внесе 2 карактери и големина на низа.
# Потоа да се отвори фајл “izlez.txt” и во
# него да се запише низа генерирана од карактерите
# што ги внел корисникот наизменично. Притоа во
# фајлот треба да се чуваат сите низи при секое
# извршување на програмата.

# primer vlez:
# + - 5 -> + - + - +
# 1 2 10 -> 1 2 1 2 1 2 1 2 1 2

f1 = open("files/izlez.txt", "a")
list = str()

a = input()
b = input()
c = int(input())

for i in range(c):
    if i % 2 == 0:
        x = a
    else:
        x = b
    list += x

f1.write(list+"\n")

f1.close()





# 6. Да се напише програма која ќе отвори некоја
# датотека и ќе изброи колку линии има, колку зборови
# и колку карактери.

# 7. Да се напише програма која ќе симулира телефонски
# именик. На почеток корисникот ќе внесе колку
# телефонски броеви ќе внесува и потоа како ќе ги
# внесува телефонските броеви така тие ќе се
# запишуваат во датотека. За секој телефонски број
# корисникот треба да пополни име, презиме и
# телефонски број.

# 8.Да се напише програма која ќе чита од некоја
# датотека текст со повеќе линии, каде секоја линија
# не завршува на “.” и секоја линија не почнува со
# голема буква. Да се запише истиот текст во друга
# датотека но со почетни големи букви и после секој
# ред да стои “.”
