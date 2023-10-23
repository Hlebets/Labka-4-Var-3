from BookLib import Book, Library

library = Library()

print("Лабораторна Робота №4 Варіант 3")
print("Кобрин Гліб, ІКСМ-1, Навчальна група №2")

while True:
    main_input = input("Оскільки даний код - Бібліотека, то прошу обрати команду для виконання: "
                       "\n1.Додати запис книги"
                       "\n2.Видалити запис книги"
                       "\n3.Переглянути усі записи книг"
                       "\n4.Вийти"
                       "\nВведіть число бажаної команди: ")

    if main_input == "1":
        name = input("Введіть назву книги, яку ви хочете додати: ")
        while True:
            pages_qty = int(input("Введіть кількість сторінок у книзі: "))
            pages_read = int(input("Введіть кількість прочитаних сторінок: "))
            if pages_read <= pages_qty:
                new_book = Book(name, pages_qty, pages_read)
                library.add_book(new_book)
                print("Книга була успішно додана")
                break
            else:
                print("Неможливо прочитати більше сторінок, ніж є в книзі. Повернення до вводу сторінок")
    elif main_input == "2":
        library.display_book_list()
        book_num = int(input("Введіть номер книжки у списку для видалення: "))
        if 1 <= book_num <= len(library.book_list):
            delete_book_by_num = library.book_list[book_num - 1]
            library.delete_book(delete_book_by_num)
            print(f"Книга під номером {book_num} була успішно видалена")
        else:
            "Книги з таким номером немає у бібліотеці"
    elif main_input == "3":
        library.display_book_list()
    elif main_input == "4":
        break
    else:
        print("Ви ввели неправильне значення, повернення до початкового запиту (дані збережені)")

