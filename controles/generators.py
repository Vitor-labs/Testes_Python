import sys

generator2 = (i for i in range(1000) if i % 2 == 0)
#print("generator2:", generator2)
print(sys.getsizeof(generator2))

mylist = [i for i in range(1000) if i % 2 == 0]
#print("mylist:", mylist)
print(sys.getsizeof(mylist))


def mygenerator():
    yield 1
    yield 2
    yield 3


g = mygenerator()

print(sum(g))

for _ in g:
    print(_)


# print(next(g))
# print(next(g))


def countdown(n):
    print("Counting down from", n)
    while n > 0:
        yield n
        n -= 1


cd = countdown(5)
next(cd)
