# try:
#     while True:
#         number = int(input('bir sandy jazihiz'))
#         if number == "Exit":
#             print('finished ...')
#             break
#         print(number ** 2)
# except:
#     print("sandy jaziniz")
#
# try:
#     while True:
#         number = int(input('bir sandy jazynyz:'))
#         number2 = int(input('bir san jaziniz:'))
#
#         if number == 'Exit':
#             print('finished ...')
#             break
#
#         print(number / namber2)
# except ZeroDivisionError:
#     print('divishion by zero')
# except ValueError:
#     print('invalid literal for int()')
#
# try:
#     number = int(input('bir sandy jaziniz'))
#     print(number ** 2)
# except ValueError:
#     print("sandy jaziniz")
# finally:
#     print("!!!")

calculator = (input("выберите функцию: (+), (-), (/), (*)"))
number1 = (input("биринчи санды жазыныз"))
number2 = (input("экинчи санды жазыныз"))
if calculator == "+":
    print(number1 + number2)

if calculator == "-":
    print(number1 - number2)

if calculator == "/":
    print(number1 / number2)

if calculator == "*":
    print(number1 * number2)





