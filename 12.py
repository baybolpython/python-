# 5! 1 * 2 * 3 * 4 * 5
# def factorial_recursive(n):
#     if n == 1:
#         return n
#     else:
#         return n*factorial_recursive(n-1)
#
# a = int(input("Enter "))
# b = factorial_recursive(a)
# print(b)

"""
     первый вызов
def factorial_recursive(n):
    if 3 == 1:
        return 3
    else:
        return 3*factorial_recursive(3-1)
        
a = factorial_recursive(3)
print(a)


      второй вызов        
        
def factorial_recursive(n):
    if 2 == 1:
        return 3
    else:
        return 3*factorial_recursive(3-1)
        
a = factorial_recursive(3)
print(a)


"""

# def person(**name):
#     for key, value in name.items():
#         print(f"{key} = {value}")
#
# person(first_name="asan", second_name="baybol")

# def get_max(numbers):
#     max_number = numbers[0]
#     for num in numbers:
#         if num > max_number:
#             max_number = num
#     return max_number
#
#
# numbers = input("Enter:")
# max_num = get_max(numbers)
# print("Самое большое число:", max_num)
i = 0
my_list = [1085764, 0, 12]
def get_sum(my_list: list):
    counter = 0
    for i in my_list:
        counter += i
    return counter
print(get_sum(my_list))







