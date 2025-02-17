from abc import ABC, abstractmethod
from .book import Book

class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        """Додає книгу в бібліотеку"""
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        """Видаляє книгу з бібліотеки за назвою"""
        pass

    @abstractmethod
    def show_books(self) -> None:
        """Відображає список книг у бібліотеці"""
        pass
