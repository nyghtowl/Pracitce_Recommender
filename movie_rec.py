'''
Example Movie Recommender

'''

import itertools
import json
import pandas as pd

class Recommender:

    def __init__(self, file):
        self.product_data = json.loads(file)
        self.users = self._find_unique_users()

    def _find_unique_users(self):
        user_list = [[review['customer'] for review in product['reviews']] for product_id, product in self.product_data.iteritems()]
        return set(itertools.chain(*user_list))

    def create_user_table(self):
        user_table = {}
        for i, user in enumerate(self.users):
            user_table[user] = i
        self.lookup_user = user_table

