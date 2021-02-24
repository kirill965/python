#!/usr/bin/env python3

import sys
if len(sys.argv) == 1:
    user_ = input("Please enter your name here: \n-> ")
else:
    user_ = sys.argv[1]

if __name__ == "__main__":
    print(f'Hello, {user_.title()}! How are you?')
