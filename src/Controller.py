from model.Book import Book
from sorting.SortingService import SortingService

class Controller:

    _sorting_service = SortingService()

    def __init__(self):
        self._books = list()
        self._sorting_params = list()    

    def _get_books(self):
        self._books.append(Book(1, 'Java How To Program', 'Deitel & Deitel', 2007))
        self._books.append(Book(2, 'Patterns of Enterprise Application Architecture', 'Martin Fowler', 2002))
        self._books.append(Book(3, 'Head First Design Patterns', 'Elisabeth Freeman', 2004))
        self._books.append(Book(4, 'Internet & World Wide Web: How to Program', 'Deitel & Deitel', 2007))

    def _get_ordering_params(self):
        self._sorting_params.append('Edition_dsc')
        self._sorting_params.append('author_DSC')
        self._sorting_params.append('Title_asc')
        

    def start_ordering(self):
        self._get_books()
        self._get_ordering_params()

        sorted_books = self._sorting_service.sort(self._books, self._sorting_params)

        for book in sorted_books:
            print(book)

        

