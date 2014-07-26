'''
Example Movie Recommender

'''

import itertools
import json
import pandas as pd
import numpy as np

class Recommender:

    def __init__(self, file):
        self.product_data = json.loads(file)
        self.users = self._find_unique_users()
        self.products = self._find_product_asin()

    def _find_unique_users(self):
        user_list = [[review['customer'] for review in product['reviews']] for product_id, product in self.product_data.iteritems()]
        return set(itertools.chain(*user_list))

    def _find_product_asin(self):
        return set([product['asin'] for product_id, product in self.product_data.iteritems()])

    def create_user_table(self):
        user_table = {}
        for i, user in enumerate(self.users):
            user_table[user] = i
        self.lookup_user = user_table


    def create_user_table2(self):
        self.lookup_user2 = pd.DataFrame(np.range(0, len(self.isers), columns=["Positions"], index=self.users)

    def create_product_table(self): 
        product_table = {}
        for i, product in enumerate(self.products):
            product_table[product] = i
        self.lookup_product = product_table

    def create_product_table2(self):
        self.lookup_product2 = pd.DataFrame(np.range(0,len(self.products))index=self.products)


    def build_feature_matrix(self):
        self.feature_matrix = np.zeros((len(self.products),len(self.users))) - 1

        for pid, product in self.product_data.iteritems():
            row = self.lookup_product[pid]

            for review in product['reviews']:
                self.feature_matrix[row,self.lookup_user[review['customer']]] = float(review['rating'])

