# from inspect import signature
from random import randint
from faker import Faker

def rand_ratio():
    return randint(840, 900), randint(473, 573)

fake = Faker('pt-BR')
# print(signature(fake.random_number))

def make_recipe():
    pass