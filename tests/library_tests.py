from loguru import logger
import pytest
from solid_library.library import Library
from solid_library.library_manager import LibraryManager
from solid_library.book import Book

def test_show_books():
    library = Library()
    manager = LibraryManager(library)
    book1 = Book("Effective Python", "Brett Slatkin", 2015)
    book2 = Book("Automate the Boring Stuff with Python", "Al Sweigart", 2015)

    manager.add_book(book1.title, book1.author, book1.year)
    manager.add_book(book2.title, book2.author, book2.year)

    log_messages = []

    # Перехоплюємо логування loguru
    def log_sink(message):
        log_messages.append(message.strip())

    logger.add(log_sink, format="{message}")

    manager.show_books()

    assert any("Effective Python" in msg for msg in log_messages)
    assert any("Automate the Boring Stuff with Python" in msg for msg in log_messages)
