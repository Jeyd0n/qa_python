from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_existed_book_len_not_change(self):
        collector = BooksCollector()

        collector.add_new_book(
            name='Гордость и предубеждение и зомби'
        )
        collector.add_new_book(
            name='Гордость и предубеждение и зомби'
        )

        assert len(collector.get_books_rating()) == 1

    def test_set_book_genre_set_genre_for_each_book(self):
        collector = BooksCollector()

        collector.add_new_book(
            name='Гордость и предубеждение и зомби'
        )
        collector.set_book_genre(
            name='Гордость и предубеждение и зомби',
            genre='Фантастика'
        )

        collector.add_new_book(
            name='Что делать, если ваш кот хочет вас убить',
        )
        collector.set_book_genre(
            name='Что делать, если ваш кот хочет вас убить',
            genre='Детективы'
        )

        assert collector.get_book_genre(
            name='Гордость и предубеждение и зомби'
        ) == 'Фантастика' and collector.get_book_genre(
            name='Что делать, если ваш кот хочет вас убить'
        ) == 'Детективы'

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