def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()

# for i in g:
#     print(i)

# value = next(g)
# print(value)

# value = next(g)
# print(value)

# value = next(g)
# print(value)


# print(sum(g))

print(sorted(g))


""" ------------------------------ """

def countdown(num):
    print("Starting to count from", num)
    while num > 0:
        yield num
        num -= 1

cd = countdown(5)

value = next(cd)
print(value)
value = next(cd)
print(value)
value = next(cd)
print(value)
value = next(cd)
print(value)
value = next(cd)
print(value)



""" -------------------------- """
import sys

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

# mylist = firstn(10)
# print(sum(mylist))

def first_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sys.getsizeof(firstn(1000000)))
print(sum(first_generator(10)))
print(sys.getsizeof(first_generator(1000000)))


""" -------------------------- """


def fibonacci(limit):
    a = 0
    b = 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = list(fibonacci(30))
print(fib)



""" -------------------------- """
import sys

mygenerator = (i for i in range(30) if i%2 == 0)
for i in mygenerator:
    print(i)
print("Size: ",sys.getsizeof(mygenerator))

print()
mylist = [i for i in range(30) if i%2 == 0]
print(mylist)
print("Size: ", sys.getsizeof(mylist))