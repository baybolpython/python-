# def print_hello():
#     print("hello")
#
# print_hello()
#
# def name(name):
#     print(f"hello {name}")
#
# name("mile")
# name("mike")
# name("mige")
# name("mihe")
# name("mite")
# name("mikr")

# def get_square(lenght, width):
#     s = lenght * width
#     print(s)
#
# get_square(234, 456)
# get_square(244, 656)

# def person(name, nickname="askarov"):
#     print(f"name: {name}/n"
#           f"nickname: {nickname}")
#
#
# person("asan", "55565")
# print()
# person(nickname="asanov", name="baybol")

# def number_input("выберите функцию"(num1, num2)):
#     num1 = input("напишите первое число:")
#     num2 = input("напишите второе число:")

def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Ошибка! Деление на ноль."
        return num1 / num2
    else:
        return "Неверная операция."

num1 = float(input("Введите первое число: "))
operation = input("Выберите операцию (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

result = calculator(num1, num2, operation)
print("Результат:", result)


