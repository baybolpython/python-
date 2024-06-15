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
# print(number)

# fruits = set(["apple", "banana", "cherry"])
# fruits1 = {"apple", "banana", "Mango"}
#
# print(fruits.union(fruits1))
# print(fruits.difference(fruits1))
# print(fruits1.difference(fruits))
# print(fruits.intersection(fruits1))
# print(fruits.symmetric_difference(fruits1))
#
# name = [1, 2, 3]
# print(set(name))


"""
 ТЕМА: DICT --- {}
"""

# person = {"Name": "Musa", "Surname": "Bakytbekov", "Age": 21}
# print(person)
# print(person['Name'])
# person["Name"] = "Adil"
# print(person)
#
# print(person.keys())
# print(person.values())
#
# del person["Name"]
# print(person)
#
# person["hobby"] = "To sing"
# print(person)

# print(ord("n"))
# print(ord("N"))

#
#
# person = [
#     {
#         "Name": "Musa",
#         "Surname": "Bakytbekov",
#         "Age": 21
#     },
#
#     {
#         "Name": "Islam",
#         "Surname": "Asanov",
#         "Age": 26
#     },
#
#     {
#         "Name": "Baibol",
#         "Surname": "Amanov",
#         "Age": 19
#     }
# ]
#
# person1 = ({"Name": "Bayel", "Surname": "Bakytov", "Age": 16})
# person2 = ({"Name": "Emir", "Surname":  "Baymanov", "Age": 18})
# person.extend(person1)
# person.extend(person2)
# # for i in person:
# #     print(i["Name"])
# #     print(
#
# print(person)

def find_min(numbers):
    min_number = numbers[0]
    for num in numbers:
        if num < min_number:
            min_number = num
    return min_number


numbers = [1, 0, 90999, 8, 34]
min_num = find_min(numbers)
print("Самое маленькое число:", min_num)






