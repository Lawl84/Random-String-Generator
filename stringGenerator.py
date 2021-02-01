import random # We need to import random to pick a random character.


def randomString(length:int, numberOfStrings= 1): # randomString definition

    string = [''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZY1234567890~!@#$%^&*()_+-=\'".,') for i in range(length)])
             for i in range(numberOfStrings)] # Generates a random sequence of strings

    return string
#returns a list of the string(s)
