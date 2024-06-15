"""
    Текст менен иштеле турган методдор

    пер.isdigit() - жазылган элементтин баары санбы ошону текшерип берет.
    пер.isalpha() - жазылган элементтин баары тамгабы ошону чыгарат.
    пер.isalnum() - сан тамга аралышпы ошону текшерип берет
    пер.islower() - бардык тамга кичине болсо True деп чыгарат, бир эле тамга чон болсо False деп чыгарат
    пер.isupper() - бардык тамга чон болсо True деп чыгарат, бир эле тамга кичине болсо False деп чыгарып берет
    пер.istitle() -биринчи тамга чонбу же кичинеби текшерет
    пер.lower() - тамгалардын баарын кичине кылып салат
    пер.upper() - тамгалардын баарын чон кылып салат
    пер.startwith(Hi) - баштапкы тамгаларды текшерсе болот
    пер.endswith(12) - акыркы соз кайсыл тамга менен бутконун текшерет
    пер.split() -  текстти листке айландырват
    пер.replace(баштапкы маани, кайсыл созго озгортобуз) - Созду озгортуп берет

    пер - бул переменный
"""

# a = "126A"
# print(a.isdigit())

# b = "Asan12"
# print(b.isalpha())
#
# c = "Asan27"
# print(c.isalnum())

# cd = "saNa"
# print(cd.islower())

# cd = "AsaN"
# print(cd.lower())
# print(cd.istitle())
# print(cd.isupper())

# name = input("Atynyz: ")
# print(name.lower())
# print(name.upper())



#
# print(NumText.split())NumText = "Hi 123 Sanjar"
# print(f"replaceке чейин: {NumText}")
# print("replaceке колдонгондон кийин: ", NumText.replace("123", "Asan"))
# text = "Hello123"
# print(text.startswith("He"))
# print(text.endswith("423"))

# while True:
#     world = input("Enter your text: ")
#
#     if world == "Exit":
#         print("Finished ... ")
#         break
#
#     world = world.lower()
#     print(world.split())

# while True:
#     i = input("ведите число=")
#
#     print(i[:: -1])
#
number = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# i = 0
# j = 0
#
#
# while i < len(number):
#     print(number[i][j])
#     i += 1
#     j = (j + 1) % 2


i = 0
j = 0

while i < len(number):
    print(number[i][j])
    if j == 1:
        j -= 2
    i += 1
    j += 1