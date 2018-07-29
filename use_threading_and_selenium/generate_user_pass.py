import os
import random
import string


def generate_user():
	number = '{:10d}'.format(random.randrange(1, 9999999999))
	name = 'raisalimaputriayu'
	username = name + number
	return username

def generate_pw():
    length = random.randint(6,20) - 10
    pwd = []
    pwd.append(random.choice(string.ascii_lowercase))
    pwd.append(random.choice(string.ascii_uppercase))
    pwd.append(str(random.randint(0,9)))
    pwd.append(random.choice.length)
    # fill out the rest of the characters
    # using whatever algorithm you want
    # for the next "length" characters
    # random.choice.length
    random.shuffle(pwd)
    return ''.join(pwd)


def generate_pw2(length=15, charset="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"):
    return "".join([random.choice(charset) for _ in range(0, length)])