from main import BooksCollector
import pytest


TEST_SET_BOOK_GENRE_SET_SINGLE_BOOK_GENRE_PARAMS = [
    ['Гордость и предубеждение и зомби', 'Фантастика'],
    ['Что делать, если ваш кот хочет вас убить', 'Детективы']
]


class TestBooksCollector:
    
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.books_genre) == 2

    def test_add_new_book_add_existed_book_len_not_change(
        self
    ):
        collector = BooksCollector()

        collector.add_new_book(
            name='Гордость и предубеждение и зомби'
        )
        collector.add_new_book(
            name='Гордость и предубеждение и зомби'
        )

        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize(
        'book_name, book_genre',
        TEST_SET_BOOK_GENRE_SET_SINGLE_BOOK_GENRE_PARAMS
    )
    def test_set_book_genre_set_single_book_genre(
        self,
        book_name: str,
        book_genre: str
    ):
        collector = BooksCollector()

        collector.add_new_book(
            name=book_name
        )
        collector.set_book_genre(
            name=book_name,
            genre=book_genre
        )

        assert collector.get_book_genre(
            name=book_name
        ) == book_genre

    def test_(self):
        ...

    def test_(self):
        ...

    def test_(self):
        ...

    def test_(self):
        ...

    def test_(self):
        ...

    def test_(self):
        ...

    def test_(self):
        ...

    def test_(self):
        ...

    def test_(self):
        ...