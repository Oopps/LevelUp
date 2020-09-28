import json


class User:
    USER_KEYS = ['name', 'surename', 'age']

    def __init__(self, name, surename, age, *args, **kwargs):
        self.name = name
        self.surename = surename
        self.age = age


class Employee(User):
    USER_KEYS = ['name', 'surename', 'age', 'company', 'position']

    def __init__(self, name, surename, age, company, position, *args, **kwargs):
        super().__init__(name, surename, age)
        self.company = company
        self.position = position


class Student(User):
    USER_KEYS = ['name', 'surename', 'age', 'university', 'course', 'id']

    def __init__(self, name, surename, age, university, course, id, *args, **kwargs):
        super().__init__(name, surename, age)
        self.university = university
        self.course = course
        self.id = id


def valid_file(path):
    created = []
    with open(path) as f:
        data = json.load(f)
        for i in data:
            s = list(i.keys())
            if Student.USER_KEYS == s:
                created.append(Student(**i))
            elif Employee.USER_KEYS == s:
                created.append(Employee(**i))
            elif User.USER_KEYS == s:
                created.append(User(**i))
            else:
                continue

    print(created)


valid_file('1.txt')
