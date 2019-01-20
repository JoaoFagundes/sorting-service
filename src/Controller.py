import configparser
import json

from src.model.Book import Book
from src.sorting.SortingService import SortingService, OrderingException

class Controller:

    _sorting_service = SortingService()

    def __init__(self):
        self._books = []
        self._sorting_params = []  
        self._parser = configparser.SafeConfigParser() 

    def _get_books(self, filename='books_list.json'):
        """
            Opens the books_list.json file to instantiate the books.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            
            for book in data['books']:
                book_id = book['id']
                title = book['title']
                author = book['author']
                edition = book['edition']

                self._books.append(Book(book_id, title, author, edition))

        except json.decoder.JSONDecodeError:
            pass

    def _get_sorting_params(self, filename='.config'):
        """
            Opens the .config file to get the sorting parameters.
        """
        params = self._read_sorting_params(filename)
        self._sorting_params = list()

        if '' in params:
            return
        
        for param in params:
            self._sorting_params.append(param)

    def _read_sorting_params(self, filename):
        try:
            self._parser.read(filename)
            params = self._parser.get('sorting params', 'params').split(", ")
            return params
        except configparser.DuplicateOptionError:
            raise OrderingException("You can't define more than one 'params' variable.")
        except configparser.NoOptionError:
            raise OrderingException("You need to insert sorting parameters under 'sorting params'.")
        

    def start_sorting(self):
        self._get_books()
        self._get_sorting_params()

        sorted_books = self._sorting_service.sort(self._books, self._sorting_params)

        for book in sorted_books:
            print(book)

        

