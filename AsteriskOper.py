# ***************

result = 2**7
print(result)

""" ---------------------------------------------------------------- """

zeroes = [0]*10
print(zeroes)

zeroOnes = [0, 1] * 10
print(zeroOnes)

ZeroesTpl = (0, 1) * 10
print(ZeroesTpl)

string = "Black-D3vil "*10
print(string)

""" ---------------------------------------------------------------- """

numbers = [1, 2, 3, 4, 5, 6]

*beginning, last = numbers
print(beginning)
print(last)



""" ---------------------------------------------------------------- """

numbers = [1, 2, 3, 4, 5, 6]

beginning, *middle, secondLast, last = numbers
print(beginning)
print(middle)
print(secondLast)
print(last)


""" ---------------------------------------------------------------- """

my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}

new_list = [*my_tuple, *my_list, *my_set]

print(new_list)

new_tuple = (*my_tuple, *my_list, *my_set)
print(new_tuple)


dict_a = {'a': 1, 'b': 2, 'c': 3}
dict_b = {'d': 4, 'e': 5}

new_dict = {**dict_a, **dict_b}
print(new_dict)