'''
Example Movie Recommender

'''

class Recommender:

    def __init__(self, products_file):
        self.product_data = json.loads(products_file)
        self.users = self._find_unique_users()
