from .library_interface import LibraryInterface
from .book import Book
from loguru import logger

class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logger.info(f"Книга додана: {book}")

    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                logger.info(f"Книга видалена: {book}")
                return
        logger.warning(f"Книга не знайдена: {title}")

    def show_books(self) -> None:
        if not self.books:
            logger.info("Бібліотека порожня.")
        else:
            for book in self.books:
                logger.info(book)

# Тестуємо клас
if __name__ == "__main__":
    library = Library()
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
    
    library.add_book(book1)
    library.add_book(book2)
    library.show_books()
    library.remove_book("1984")
    library.show_books()