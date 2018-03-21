#!/usr/bin/env python
# coding=utf-8
import random

def pw_gen(pw_len=8):
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    return ''.join(random.sample(s, pw_len))

print(pw_gen(int(input('How many characters in your password? '))))

