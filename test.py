import pytest

class TestBooksCollector:

    @pytest.mark.parametrize('book_name', [
        'А',
        'А' * 40
    ])
    def test_add_new_book_valid_name_length_book_added(self, collector, book_name):
        collector.add_new_book(book_name)

        assert book_name in collector.get_books_genre()

    @pytest.mark.parametrize('book_name', [
        '',
        'А' * 41
    ])
    def test_add_new_book_invalid_name_length_book_not_added(self, collector, book_name):
        collector.add_new_book(book_name)

        assert book_name not in collector.get_books_genre()

    def test_set_book_genre_existing_book_and_valid_genre_genre_set(self, collector):
        collector.add_new_book('Война и Мир')
        collector.set_book_genre('Война и Мир', 'Фантастика')

        assert collector.get_book_genre('Война и Мир') == 'Фантастика'

    def test_get_book_genre_existing_book_returns_genre(self, collector):
        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Ведьмак', 'Фантастика')

        assert collector.get_book_genre('Ведьмак') == 'Фантастика'

    def test_get_books_with_specific_genre_returns_books_with_selected_genre(self, collector):
        collector.add_new_book('Ведьмак')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Ведьмак', 'Фантастика')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Ведьмак']

    def test_get_books_genre_returns_books_genre_dictionary(self, collector):
        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Ведьмак', 'Фантастика')

        assert collector.get_books_genre() == {'Ведьмак': 'Фантастика'}

    @pytest.mark.parametrize('book_name, genre_name', [
        ['Ведьмак', 'Фантастика'],
        ['Властелин колец', 'Комедии'],
        ['Кот в сапогах', 'Мультфильмы']
    ])
    def test_get_books_for_children_book_with_allowed_genre_is_returned(
            self, collector, book_name, genre_name
    ):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)

        assert book_name in collector.get_books_for_children()

    @pytest.mark.parametrize('book_name, genre_name', [
        ['Шерлок Холмс', 'Детективы'],
        ['Оно', 'Ужасы']
    ])
    def test_get_books_for_children_book_with_age_rating_genre_is_not_returned(
            self, collector, book_name, genre_name
    ):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)

        assert book_name not in collector.get_books_for_children()

    def test_add_book_in_favorites_existing_book_book_added(self, collector):
        collector.add_new_book('Ведьмак')
        collector.add_book_in_favorites('Ведьмак')

        assert collector.get_list_of_favorites_books() == ['Ведьмак']

    def test_delete_book_from_favorites_existing_favorite_book_book_deleted(self, collector):
        collector.add_new_book('Ведьмак')
        collector.add_book_in_favorites('Ведьмак')
        collector.delete_book_from_favorites('Ведьмак')

        assert 'Ведьмак' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_returns_favorites_books(self, collector):
        collector.add_new_book('Ведьмак')
        collector.add_book_in_favorites('Ведьмак')

        assert collector.get_list_of_favorites_books() == ['Ведьмак']

    def test_add_book_in_favorites_same_book_twice_book_added_once(self, collector):
        collector.add_new_book('Ведьмак')
        collector.add_book_in_favorites('Ведьмак')
        collector.add_book_in_favorites('Ведьмак')

        assert collector.get_list_of_favorites_books() == ['Ведьмак']
