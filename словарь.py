# del - удалить
# 5.6746465 - float
# "авыываы" - str
# True - bool
# 4 - int
# != - nerovno
# sep= - razdelit
# end= - odna linia
# /n - newline
# /t - topulasia
# 5 // 3 - okkruglit
# min - nayti min el
# max - nayti max el
# abs - nayti po modulu
# pow( 5, 3) - stepen
# round - okkruglit
# not - net
# and - i
# or - ili
# break - vixod iz sikla
# continue - propustit
# [] - list
# append - djbavit
# insert - dobavit v op mesto
# extend[] - dobavit neskelko
# sort - sortirovat
# pop - ydalit
# reverse - perevorachivat
# remove - ydalit po naznacheniy
# clear - ydalit vse
# count - sovpodenia
# len - dlina spiska
# upper - choHoity
# lower - kichireytuu
# capitalize - birinchi tamgani chon
# find - tabat kaisi jerde ekenin
# split - list kiluu
# [2:] - shag
# (5,) - tuple
# {} - dict
# {'key': 'value'} - key, value
# items - vivod
# get - vivod po key
# set, frozenset - mnozhestva
# add - koshuu
# update - dobavit neskolko
# def - function
# def get_data - metod
# pass - nechego
# return - vozvrashat
# lambda - function
# open - open file
# open(data/text.txt, 'w', 'a', 'r') - write, apen, read
# file.close() - zakrit
#  write - писать инф
# apen - add inf
# read - read inf
# union - biriktiruu
# difference - jok nerseni chigaruu
# intersection - sovpodenie vivod
# symmetric_difference - nesovpodenie vivod
# random - randomniy
# randint -  biz korsotkon random
# shuffle - aralashtirma
# choice - listtin ichinen random
# filter - filtleit
# map - ozgortuu
# with open('text.txt', 'r', encoding=utf-8) as file - open file
class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value


    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._balance = value


bank = Bank('Сбербанк', 10000)
print(bank.name)
print(bank.balance)

bank.name = 'Мбанк'
bank.balance = 15000
print(bank.name)
print(bank.balance)

