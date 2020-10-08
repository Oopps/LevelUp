#
# list_a = [1,220,333,4,5]
#
#
# def func(list1, a):
#
#     for i in range(len(list1) - a):
#         s = list1.pop(a + i)
#         list1.insert(i, s)
#
#     return list1
#
#
# print(func(list_a,2))


class Conteiner:
    def __init__(self, list1):
        self.list1 = list1
        self.__counter = 0

    def __next__(self):
        if self.__counter < len(self.list1):
            item = self.list1[self.__counter]
            self.__counter += 1
            return item
        else:
            raise StopIteration

    def __getitem__(self, item):
        self.list1[item].use +=1
        return self.list1[item]


class Something:

    def __init__(self, some):
        self.__some = some
        self.use = 0

    def __str__(self):
        return str(self.__some)


a = Something(45)
b = Something(23)

c = Conteiner([a, b])

print(a.use)

print(c[0])

print(a.use)

for i in c:
    print(i)

print(a.use)
print(b.use)