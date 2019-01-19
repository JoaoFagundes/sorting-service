from OrderingException import OrderingException

class SortingService:

    def sort(self, books, ordering_params):
        for param in ordering_params:
            attribute, direction = param.split('_')
            print(attribute)
            print(self.get_param_index(attribute))
            print(direction)

    def get_param_index(self, param_name):
        if param_name.lower() == 'title':
            return 1
        elif param_name.lower() == 'author':
            return 2
        elif param_name.lower() == 'edition':
            return 3
        else:
            raise OrderingException('There is no attribute in a book named "{}"'.format(param_name))
        
            