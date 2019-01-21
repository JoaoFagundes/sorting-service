class UserInterface:
   
    def welcome(self):
        print('======= WELCOME =======\n')
        print('This is the sorting service challenge, developed by João Fagundes')
        print('This code will be executed based on the data given by:')
        print('    -"books_list.json": will provide the list of books to be sorted')
        print('    -".config": will provide the sorting parameters to sort the books')
        print('The files must be written following the given examples.')

    def menu(self):
        print('\n======= MENU =======')
        print('    1. Show list of books;')
        print('    2. Start sorting;')
        print('    0. Exit.')
        return input('Type the number of the desired option: ')

    def list_books(self, books_list, is_sorted=False):
        if is_sorted:
            print('\nFollowing the given parameters, the list of books is sorted as follows:')
        else:
            print('\nThis is the list of book available for sorting: ')

        for book in books_list:
            print(book)

    def message(self, msg):
        print(msg)