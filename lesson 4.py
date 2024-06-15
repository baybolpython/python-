# for i in range(1001):
#     if 900 < i < 950:
#         continue
#     print(i, "Bayel")
#
# for i in range(1001):
#     if i == 500:
#         break
#     print(i, "Bayel")

# world = 'привет'
# for i in world:
#     print(i)



# for i = 0
# for i in <= 10:
#     for j = 0
#     for j in range < 11:
#         print("{i} * {j} = {i * j}")
#         j += 1
#     i += 1
#     print()

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i*j}")


# i = 0
# while i < 6:
#      i += 1
#      if i == 3:
#          continue
#      print (i)

# for i  in range(10):
#     text = input('Enter your text: ').title()
#     if text == 'exit'.title() or text == 'выход'.title():
#         print('finished')
#         break
#
#     print(text)
# while True:
#     login = input("напишите ваш логин")
#     password = input("напишите ваш пароль")
#     print("напишите повторно")
#     login2 = input("напишите ваш логин")
#     password2 = input("напишите ваш пароль")
#     if login == login2 and password == password2:
#         print("ввoд разрещен")
#     else:
#         print("ввод запрещен")
#     print()

# world = "hello"
# print(len(world))


login = input("напишите ваш логин: ")
password = input("напишите ваш пароль: ")
print("напишите повторно")
login2 = input("напишите ваш логин: ")
password2 = input("напишите ваш пароль: ")
if login == login2 and password == password2:
    print("ввод разрешен")
else:
    print("ввод запрещен")
print()

a = "калькулятор"
b = "твой знак зодиака"
game = input("что будем делать дальше? ")

if game == a:
    calculator()

print("Калькулятор запущен. Введите 'выход' для выхода.")
while True:
    operation = input("Выберите операцию (+, -, *, /): ")
    if operation == 'выход':
        break
    if operation in ('+', '-', '*', '/'):
        x = float(input("Введите первое число: "))
        y = float(input("Введите второе число: "))
        if operation == '+':
            print(f"Результат: {x + y}")
        elif operation == '-':
            print(f"Результат: {x - y}")
        elif operation == '*':
            print(f"Результат: {x * y}")
        elif operation == '/':
            if y != 0:
                print(f"Результат: {x / y}")
            else:
                print("Ошибка: Деление на ноль!")
        else:
            print("Неверная операция")
elif game == b:
    print("Функция определения знака зодиака ещё не реализована.")
else:
    print("Неверный выбор.")

