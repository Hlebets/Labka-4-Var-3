class Book:
    def __init__(self, name, pages_qty, pages_read):
        self.name = name
        self.pages_qty = pages_qty
        self.pages_read = pages_read

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
        for i, book in enumerate(self.book_list, start=1):
            print(f"{i}. Назва: {book.name}, Прочитано: {book.read_percent():.2f}%")
