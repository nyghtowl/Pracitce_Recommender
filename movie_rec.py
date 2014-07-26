'''
Example Movie Recommender

'''

class Recommender:

    def __init__(self, products_file):
        self.product_data = json.loads(products_file)
        self.users = set() #self._find_unique_users()

    def _find_unique_users(self):
        user_list = [[review['customer'] for review in product['reviews']] for product_id, product in self.product_data.iteritems()]
        return set(itertools.chain(*user_list))
