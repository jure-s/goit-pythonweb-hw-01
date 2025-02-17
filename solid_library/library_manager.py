from .library import Library
from .book import Book
from loguru import logger

class LibraryManager:
    def __init__(self, library: Library) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        logger.info(f"Додано книгу: {book}")

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()

# Тестуємо клас
if __name__ == "__main__":
    library = Library()
    manager = LibraryManager(library)
    
    manager.add_book("The Catcher in the Rye", "J.D. Salinger", 1951)
    manager.add_book("Brave New World", "Aldous Huxley", 1932)
    manager.show_books()
    manager.remove_book("The Catcher in the Rye")
    manager.show_books()
