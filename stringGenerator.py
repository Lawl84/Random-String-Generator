import random


def randomString(length:int, numberOfStrings= 1):

    string = [''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZY1234567890~!@#$%^&*()_+-=\'".,') for i in range(length)])
             for i in range(numberOfStrings)]

    return string
#returns a list of the string(s)
print(randomString(44))