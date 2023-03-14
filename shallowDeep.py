org = 8
cpy = org
print(org)
print(cpy)
cpy = 6
print(org)
print(cpy)

""" ---------------------------------------- """

org = [0, 1, 2, 3, 4]
cpy = org
cpy[0] = 5
print(org)
print(cpy)


""" ---------------------------------------- """

import copy

""" - shallow copy : one level deep, only reference of nested child objects 
    - deep copy : full independent copy
"""

org = [0, 1, 2, 3, 4]

# cpy = copy.copy(org)
# cpy = org.copy()
# cpy = list(org)
cpy = org[:]

cpy[0] = 5
print(org)
print(cpy)


""" ---------------------------------------- """
# Shallow Copy

import copy

org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.copy(org)
cpy[0][0] = -10
print(cpy)
print(org)

""" ---------------------------------------- """

# Deep Copy

import copy

org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][0] = -10
print(cpy)
print(org)

""" -------------------------- """

import copy 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

p1 = Person('Alex', 55)
p2 = Person('John', 30)

company = Company(p1, p2)

company_clone = copy.deepcopy(company)

company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)


""" ---------------------------------------- """

