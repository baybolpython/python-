# """
#     ТЕМА: Модул, import
# """
#
# """Собственный модули"""
#
# # import main
# # from main import print_hello, S
# # from main import your_age as age
# #
# # main.print_hello("Sagyn", "Asanov")
# # print_hello("Musa", "Sadyrov")
# #
# # main.S(256, 2568)
# # S(126, 566)
# #
# # age()
#
# """Встроенным модули"""
#
# # import random
# #
# # print(random.random())
# # print(random.randint(100, 150))
# #
# # my_list = ["Islam", "Musa", "Sanjar", "Baibol"]
# # random.shuffle(my_list)
# # print(my_list)
# #
# # choice_name = random.choice(my_list)
# # print(choice_name)
#
#
# """Внешние модули"""
#
#
#
# """
#     ТЕМА: Файлдар менен иштешүү
# """
#
# file = open("shirek.txt", "w")
# file.write("Hi pupils")
# file.close()
#
# with open("shirek.txt", "a") as file_shirek:
#     file_shirek.write("\nвторая строка")
#
# # with open("shirek.txt", "x") as file_x:
# #     file_x.write("\n126")
#
# with open("shirek.txt", "r") as file_read:
#     # print(file_read.read())
#     print(file_read.readlines())
#
#



def display_result(value):
    print(value)

def power_of_number(base, exponent):
    from math import pow
    return pow(base, exponent)

def random_function(1st):
    from random import shuffle
    shuffle(1st)
    return 1st







