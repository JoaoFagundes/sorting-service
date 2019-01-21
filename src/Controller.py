import configparser
import json

from ui.UserInterface import UserInterface
from src.model.Book import Book
from src.sorting.SortingService import SortingService, OrderingException

class Controller:

    _sorting_service = SortingService()
    _ui = UserInterface()

    def __init__(self):
        self._books = list()
        self._sorting_params = list()  
        self._parser = configparser.SafeConfigParser()

    def _fill_book_list(self, filename='books_list.json'):
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

    def _fill_sorting_params(self, filename='.config'):
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

    def option_menu(self):      
        while True:
            selected_option = int(self._ui.menu())
            if selected_option not in [0, 1, 2]:
                self._ui.message('Please insert a valid option.')
            elif selected_option == 1:
                self._ui.list_books(self._books)
            elif selected_option == 2:
                self.start_sorting()
                self._ui.message('\nFinished sorting. Exiting program.')
                break
            else:
                self._ui.message('Exiting...')
                break

    def start_sorting(self):
        self._fill_sorting_params()
        sorted_books = self._sorting_service.sort(self._books, self._sorting_params)
        self._ui.list_books(sorted_books, True)

    def start_client(self):
        self._fill_book_list()
        self._ui.welcome()
        self.option_menu()


        

