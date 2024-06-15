# def print_hello(name, surname):
#     print(f"Hello {name} {surname}")
#
# def S(a, b=1000):
#     print(a * b)
#
# def your_age():
#     age = int(input("Сиздин жашыныз канчада? "))
#
#     if age < 16:
#         print("Сизге паспорт берилбейт")
#     else:
#         print("Сизге паспорт берилет")

from 15 import display_result, power_of_number, random_function

display_result("Привет, мир!")

result = power_of_number(2, 3)
display_result(result)

my_list = [1, 2, 3, 4, 5]
shuffled_list = random_function(my_list)
display_result(shuffled_list)








