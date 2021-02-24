#!/usr/bin/env python3

#Creation of simple hello function
def hello_(name):
    """Print hello, to the name."""
    return f'Hello, {name.title()}.'

if __name__ == "__main__":
    print(hello_(input("Enter your name, please: ")))
