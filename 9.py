# first = []
#
# for x in range(1, 5):
#   for y in range(5, 1, -1):
#     if x != y:
#       first.append((x, y))
#
# second = [(x, y) for x in range(1, 5) for y in range(5, 1, -1) if x != y]
#
#     first == second
#     True
# numbers = [-3, -2, -1, 0, 1, 2, 3]
# positive_numbers = [n for n in numbers if n > 0]
#
# print(positive_numbers)
# dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
# words = [word for word in dictionary]
# print(words)    # ['red', 'blue', 'green']
# my_list = []
#
# word = int(input("напишите лист:"))
#
# a = "append"
# b = "remove"
# list = input("что дальше?")
#
# if game == a:

"""
    ТЕМА: Кортеж - tuple --- ()
    Set - {}
"""

# name = ("Asan", "Batma", "Sanjar", "Islam")
# # print(type(name))
#
# print(name.index("Batma"))
# print(name.count("Musa"))
# print(name[2])


#
# name = "Asan", "Batma", "Sanjar", "Islam"
# print(type(name))
#
# number1 = 1
# number2 = 1,
#
# print(f"1 --- {type(number1)}")
# print(f"1, --- {type(number2)}")

# object = True, False, 1, 12, "Musa"
# print(type(object))



"""
    ТЕМА: SET --- {}
"""

# number = {1, 1, 1, False, 0, 2, 5, 6, 7, 7, 8, True}
#
#
# # a = number.add(34)
# print(number.add(23))
#
# print(number)

my_list = []
for i in range(1, 101):
    print(i)
