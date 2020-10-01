import os


path1 = "/home/user/Загрузки"


# class DirIter:
#
#     def __init__(self, path):
#         self.__path = path
#         self.__dirs = os.listdir(path)
#         self.__counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__counter < len(self.__dirs):
#             os_item = self.__dirs[self.__counter]
#             self.__counter += 1
#             return os_item
#         else:
#             raise StopIteration
#
#     def __getitem__(self, item):
#         return self.__dirs[item]
#
#
#
# a = DirIter(path1)
# #
# # print(a.dirs)
#
# for i in a:
#     print(i)




class File:
    def __init__(self, path):
        self.path = path

    def find_and_replace(self, new_file_name):
        f = open(self.path, 'r')
        file_text = f.read()
        file_list = list(file_text)
        file_set = set(file_list)
        max_symbol = ''
        max_symbol_qty = 0
        for i in file_set:
            symbol_counter = file_list.count(i)
            if symbol_counter > max_symbol_qty:
                max_symbol = i
                max_symbol_qty = symbol_counter

        z = open(new_file_name, 'w')
        z.write(file_text.replace(max_symbol, '*'))
        z.close()

        return print(f'Max symbol was {max_symbol} in {max_symbol_qty} q-ty')



a = File('1.txt')

a.find_and_replace('2.txt')