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
        self.products = set()

    def _find_unique_users(self):
        user_list = [[review['customer'] for review in product['reviews']] for product_id, product in self.product_data.iteritems()]
        return set(itertools.chain(*user_list))

    def create_user_table(self):
        user_table = {}
        for i, user in enumerate(self.users):
            user_table[user] = i
        self.lookup_user = user_table


    def create_user_table2(self):
        self.lookup_user2 = pd.DataFrame(columns=[Ratings], index=self.users)

    def create_product_table(self): 
        product_table = {}
        for i, product in enumerate(self.products):
            product_table[product] = i
        self.lookup_product = product_table

    def create_product_table2(self):
        self.lookup_product2 = pd.DataFrame(index=self.products)