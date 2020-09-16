import os


path1 = "/media/sf_Python/tmp/"


class FileSorter:

    path = ''
    dirs = []
    split_dirs = []

    def __init__(self, path):
        self.path = path
        self.dirs = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        for i in self.dirs:
            a = i.split('.')
            self.split_dirs.append(a[-1])

    def sort(self):
        dir_count, file_count = 0, 0

        dirs_name = set(self.split_dirs)

        for i in dirs_name:
            if not os.path.isdir(self.path + i):
                os.mkdir(self.path+i)
                dir_count += 1
            for j in self.dirs:
                if j.endswith('.' + i):
                    if not os.path.isfile(self.path + i + '/' + j):
                        os.rename(self.path + j, self.path + i + '/' + j)
                        file_count += 1
        return f'{file_count} files was sorted into {dir_count} folders'


a = FileSorter(path1)

print(a.sort())

