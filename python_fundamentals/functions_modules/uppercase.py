#!/usr/bin/env python3


def uppercase(str):
    result = ""
    for character in str:
        code = ord(character)
        if 97 <= code <= 122:
            code -= 32
        result += chr(code)
    print(result)
