from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_existed_book_len_not_change(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_rating()) == 1

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

    def test_(self):
        ...