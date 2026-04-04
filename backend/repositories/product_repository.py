

class ProductRepository:
    def __init__(self,db_pool):
        self.db_pool = db_pool
    
    # returns what products are exsits
    def search(self, query): pass

    # returns the stores that sell the products, can be called after search
    def get_stores_by_product(self,product_id): pass



