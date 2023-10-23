class Book:
    def __init__(self, name, pages_qty):
        self.name = name
        self.pages_qty = pages_qty
        self.pages_read = 0

    def to_read(self, pages):
        if self.pages_read + pages <= self.pages_qty:
            self.pages_read += pages
        else:
            print("Не можливо прочитати більше сторінок, ніж є в книзі.")

    def read_percent(self):
        return (self.pages_read / self.pages_qty) * 100


class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)

    def delete_book(self, book):
        if book in self.book_list:
            self.book_list.remove(book)
        else:
            print("Книга не знайдена в бібліотеці.")

    def display_book_list(self):
        for book in self.book_list:
            print(f"Назва: {book.name}, Прочитано: {book.read_percent()}%")