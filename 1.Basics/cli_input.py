#!/usr/bin/env python3

import sys

def greet(name:str):
    return f'Hello, {name}! Everything OK?'

if len(sys.argv) > 1:
    print(greet(sys.argv[1].title()))
else:
    print('Enter your name here: ')
    name = input()
    print(greet(name.title()))
