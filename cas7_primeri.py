














# === GENERALNI ISKLUCHOCI ===
# a = input()
# b = input()
#
# try:
#     print(int(a)/int(b))
# except:
#     b = 1
#     print('Cannot divide a with b')
#
# print(b)



# === SPECIFICHNI ISKLUCHOCI ===
# a = input()
# b = input()
#
# try:
#     print(int(a)/int(b))
#
# except ZeroDivisionError:
#     print("Cannot divide with 0!")


# === POVEKJE EXCEPTS ===
# a = input()
# b = input()
#
# try:
#     print(int(a)/int(b))
# except ZeroDivisionError:
#     print("Cannot divide with 0!")
# except ValueError:
#     print("Must enter two integers!")
# except Exception:
#     print("An error has occurred!")

# === POVEKJE ISKLUCHOCI VO EDEN EXCEPT ===
#
# a = input()
# b = input()
#
# try:
#     print(int(a)/int(b))
#
# except (ZeroDivisionError, ValueError):
#      print("Please enter two integers a and b, b != 0!")
#     print('greg')



# === EXCEPTION ARGUMENT ===
# a = input()
# b = input()
# try:
#     x = int(a) / int(b)
# except Exception as Argument:
#     print( 'This is the Argument: ', Argument)

# === PRIMER ===
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
#     print(i)
#
# except OSError as err:
#     print("OS error:", err)
#
# except ValueError:
#     print("Could not convert data to an integer.")
#
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)=}")


# === RAISE EXCEPTIONS ===

def fun(a, b):
    if a < 5:
        raise ValueError('Please enter a number bigger than 5')
    return a + b


a = int(input())
b = int(input())

try:
    fun(a, b)

except ValueError as e:
    print(e)