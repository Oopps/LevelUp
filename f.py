
# p = "/media/sf_Python/tmp/config.txt"


# class File:
#     def __init__(self, path):
#         self.path = path
#
#     def read(self):
#
#         f = open(self.path, 'r')
#         file_text = f.read()
#         qty_s = len(file_text)
#         qty_w = file_text.count(' ') + 1
#         qty_sent = file_text.count('.')
#         print(f'File has {qty_s} symbols, {qty_w} words and {qty_sent} sentences')
#
#
# a = File(p)
#
# a.read()


class User:

    def __init__(self, name, surename, age):
        self.name = name
        self.surename = surename
        self.age = str(age)




    def wdata(self):

        f = open(self.name + self.surename +'.txt', 'w')

        f.write(self.name + '\n')
        f.write(self.surename + '\n')
        f.write(self.age + '\n')

        f.close()

    def rdata(self, filename):
        f = open(filename, 'r')
        self.name = f.readline()
        self.surename = f.readline()
        self.age = f.readline()




a = User('Anton', 'Tymoshenko', 25)

a.wdata()

b = User('', '', '')

b.rdata('AntonTymoshenko.txt')

print(b.name)




