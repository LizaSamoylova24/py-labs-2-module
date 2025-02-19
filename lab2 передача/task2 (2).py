from task import Book
BOOKS_DATABASE = [
    {
        "id_": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id_": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]



# TODO: написать класс Book


# TODO: написать класс Library

class Library: # Это объявление класса Library

    def init(self, books = None):  # инициализация конструктора класса 
        self.books = books  # присваивание значение books атрибуту books текущего экземпляра класса
        if books == None: self.books = []  # проверка значения books, если значение нет выводит None

    def get_next_book_id(self) -> int:
        return len(self.books)+1

    def get_index_by_book_id(self, id_):
        for index, book in enumerate(self.books):
            if book.id_ == id_:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")
        return -1
        
if name == 'main':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id_"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

