from re import *
from termcolor import colored


name = input('inter you name:')
address = input('inter you email address:')
phone = input('inter you phone:')


def validateAddress(address):

    pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    is_valid = pattern.match(address)
    if is_valid:
        print('правильний email:', is_valid.group())
    else:
        print('неправильний email! введіть email...')


def validatePhone(phone):

    pattern = compile('^((8|\+38)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')
    is_valid = pattern.match(phone)
    if is_valid:
        print('правильний номер:', is_valid.group())
    else:
        print('Некоректний номер телефону')


def validateName(name):

    pattern = compile('(^|\s)[-a-z]{2,255}(\s|$)')
    is_valid = pattern.match(name)
    if is_valid:
        print('правильний name:', is_valid.group())
    else:
        print('неправильний name! введіть name...')


print('\n-----------------------------------------\n')

validateAddress(address)
validatePhone(phone)
validateName(name)