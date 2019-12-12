# base module imports
import math
import os
import sys

# third party imports
import requests


def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting


print(greet('world'))
print(greet('Jim'))

r = requests.get('http://www.brattleborofoodcoop.coop')
print(r.status_code)

if r.status_code == 200:
    print('success!')
elif r.status_code == 404:
    print('not found :(')

name = input("Your name?")
print("hello,", name)
