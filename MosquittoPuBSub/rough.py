class Suyash:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print_fullname(self):
        print(self.name + ' ' + self.surname)


def main():
    obj = Suyash('Suyash', 'Walkunde', 23)
    obj.print_fullname()


if __name__ == '__main__':
    main()
