from BookLib import Book, Library

book1 = Book(input("Введіть назву твору для першої книги, яку ви хочете додати: "), int(input("Введіть кількість сторінок у книзі: ")))
book1.to_read(int(input("Введіть кількість прочитаних сторінок: ")))
book2 = Book(input("Введіть назву твору для першої книги, яку ви хочете додати: "), int(input("Введіть кількість сторінок у книзі: ")))
book2.to_read(int(input("Введіть кількість прочитаних сторінок: ")))
library = Library()

library.add_book(book1)
library.add_book(book2)

library.display_book_list()
