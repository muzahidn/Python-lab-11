class Publication:
    def __init__(self, name):
        self.name = name 


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f'Book name: {self.name}')
        print(f'Author: {self.author}')
        print(f'Page count: {self.page_count}')


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f'Magazine Name: {self.name}')
        print(f'Chief Editor: {self.chief_editor}')


def main():
    magazine = Magazine('Donald Duck', 'Aki Hyyppä')
    book = Book('Compartment No. 6', 'Rosa Liksom', 192)

    print('Magazine:')
    magazine.print_information()
    print('')
    print('Book:')
    book.print_information()

main()
