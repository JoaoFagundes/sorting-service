class Book:

    def __init__(self, book_id, title, author, edition):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._edition = edition

    def __str__(self):
        return 'Book #{} - {}, {} ({})'.format(self._book_id, self._title, self._author, self._edition)

    def get_id(self):
        return self._book_id

    def get_title(self):
        return self._title
    
    def get_author(self):
        return self._author

    def get_edition(self):
        return self._edition