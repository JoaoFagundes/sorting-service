from operator import attrgetter
from src.sorting.OrderingException import OrderingException

class SortingService:

    _valid_attributes = ['title', 'author', 'edition']
    _valid_directions = ['asc', 'dsc']

    def sort(self, books, sorting_params):
        
        '''
            If no params are given in .config file, the sorting process must return
            an empty books list.
        '''
        if sorting_params == list():
            return list()

        
        '''
            Since python sorting methods are guaranteed to be stable, we start sorting
            from the last given parameter to the first. For more information read about
            'stable sort'.
        '''
        for param in reversed(sorting_params):
            attribute, direction = param.split('_')
            self.check_valid_params(attribute, direction)

            reverse_direction = (True if direction.lower() == 'dsc' else False)
            books.sort(key=attrgetter(''.join(['_', attribute.lower()])), reverse=reverse_direction)
            
        return books

    def check_valid_params(self, attribute, direction):
        '''
            In case an attribute or sorting direction is mistyped in the configuration
            file, this method will raise an OrderingException with the appropriate message.
        '''
        if attribute.lower() not in self._valid_attributes:
            raise OrderingException('"{}" is not a valid book attribute.'.format(attribute))
        if direction.lower() not in self._valid_directions:
            raise OrderingException('"{}" is not a valid sorting direction.'.format(direction))
