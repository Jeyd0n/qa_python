from main import BooksCollector
import pytest


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
        [
            ['Гордость и предубеждение и зомби', 'Фантастика'],
            ['Что делать, если ваш кот хочет вас убить', 'Детективы']
        ]
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

        # Так получается, что я тестирую сразу два метода, которые отдельные друг от друга и не тестируются. 
        # Нужно ли писать два разных теста для них или можно сделать так, как в этом тесте? Какое название тогда ставить?
        assert collector.get_book_genre(
            name=book_name
        ) == book_genre

    # Как называть метод, если название функции дублирует тестируемый функционал?
    def test_get_books_genre_get_books_genre(
        self,
        books
    ):
        collector = BooksCollector()

        for book_name, book_genre in books.items():
            collector.add_new_book(
                name=book_name
            )
            collector.set_book_genre(
                name=book_name,
                genre=book_genre
            )

        books_genre = collector.get_books_genre()

        assert books == books_genre
        
    @pytest.mark.parametrize(
        'genre', 
        [
            'Фантастика',
            'Ужасы',
            'Детективы',
            'Мультфильмы',
            'Комедии'
        ]
    )
    def test_get_books_with_specific_genre_get_books_with_specific_genre(
        self,
        genre,
        books
    ):
        collector = BooksCollector()

        for book_name, book_genre in books.items():
            collector.add_new_book(
                name=book_name
            )
            collector.set_book_genre(
                name=book_name,
                genre=book_genre
            )

        books_with_specific_genre_books = collector.get_books_with_specific_genre(
            genre=genre
        )
        books_with_required_genre = [

        ]
        for book_name, book_genre in books.items():
            if book_genre == genre:
                books_with_required_genre.append(book_name)

        for book_name in books_with_required_genre:
            assert book_name in books_with_specific_genre_books

    def test_get_books_for_children_get_books_for_children(
        self,
        books
    ):
        collector = BooksCollector()

        for book_name, book_genre in books.items():
            collector.add_new_book(
                name=book_name
            )
            collector.set_book_genre(
                name=book_name,
                genre=book_genre
            )

        books_for_children = collector.get_books_for_children()
        filtered_books = [

        ]
        for book_name, book_genre in books.items():
            if book_genre not in collector.genre_age_rating:
                filtered_books.append(book_name)

        for book_name in filtered_books:
            assert book_name in books_for_children

    def test_add_book_in_favorites_add_two_books(
        self
    ):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.favorites) == 2

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