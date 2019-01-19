from model.Book import Book
from sorting.SortingService import SortingService

class Controller:

    __sorting_service = SortingService()

    def __init__(self):
        self.__books = list()
        self.__ordering_params = list()    

    def _get_books(self):
        self.__books.append(Book(1, 'Java', 'Bla', 2001))  
        self.__books.append(Book(2, '2', '2', 2002))
        self.__books.append(Book(3, '3', '3', 2003))


    def _get_ordering_params(self):
        self.__ordering_params.append('Author_ASC')
        self.__ordering_params.append('Title_DSC')

    def start_ordering(self):
        self._get_books()
        self._get_ordering_params()

        self.__sorting_service.sort(self.__books, self.__ordering_params)
        

