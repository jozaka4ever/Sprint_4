import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

class TestBooksCollector:
    def test_add_new_book_book_added(self, collector):
        collector.add_new_book('Война и Мир')
        assert 'Война и Мир' in collector.get_books_genre()

    def test_set_book_genre_genre_setted(self, collector):
        collector.add_new_book('Война и Мир')
        collector.set_book_genre('Война и Мир', 'Фантастика')
        assert collector.get_books_genre() == {'Война и Мир':'Фантастика'}

    def test_get_books_genre_genre_shows(self, collector):
        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Ведьмак', 'Фантастика')
        assert collector.get_book_genre('Ведьмак') == 'Фантастика'

    @pytest.mark.parametrize('book_name, genre_name',[
    ['Ведьмак', 'Фантастика'],
    ['Шерлок Холмс', 'Детективы'],
    ['Властелин колец', 'Фантастика']
])
    def test_get_books_with_specific_genre_shows_books(self, collector, book_name, genre_name):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert book_name in collector.get_books_with_specific_genre(genre_name)

    @pytest.mark.parametrize('book_name, genre_name, is_for_children',[
    ['Ведьмак', 'Фантастика', True],
    ['Шерлок Холмс', 'Детективы', False],
    ['Властелин колец', 'Фантастика', True],
    ['Оно', 'Ужасы', False]
])
    def test_get_books_for_children_allowed_genres_added(self, collector, book_name, genre_name, is_for_children):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert (book_name in collector.get_books_for_children()) == is_for_children

    def test_add_book_in_favorites_book_added(self, collector):
        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Ведьмак', 'Фантастика')
        collector.add_book_in_favorites('Ведьмак')
        assert 'Ведьмак' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_book_deleted(self, collector):
        collector.add_new_book('Ведьмак')
        collector.add_book_in_favorites('Ведьмак')
        collector.delete_book_from_favorites('Ведьмак')
        assert 'Ведьмак' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_shows_books(self, collector):
        collector.add_new_book('Ведьмак')
        collector.add_book_in_favorites('Ведьмак')
        assert collector.get_list_of_favorites_books() == ['Ведьмак']


    def test_add_book_in_favorites_cannot_be_twice(self, collector):
        collector.add_new_book('Ведьмак')
        collector.add_book_in_favorites('Ведьмак')
        collector.add_book_in_favorites('Ведьмак')
        assert len(collector.get_list_of_favorites_books()) == 1