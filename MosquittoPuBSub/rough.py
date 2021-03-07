class Deepak:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print_fullname(self):
        print(self.name + ' ' + self.surname)


def main():
    obj = Deepak('Deepak', 'Kumar', 23)
    obj.print_fullname()


if __name__ == '__main__':
    main()
