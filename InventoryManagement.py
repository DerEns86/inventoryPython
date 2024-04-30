class InventoryManagement:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def update_product(self, name, new_quantity):
        for prod in self.products:
            if prod.name == name:
                prod.quantity = new_quantity
                return True
        return False

    def remove_product(self, name):
        for prod in self.products:
            if prod.name == name:
                self.products.remove(prod)
                return True
        return False

    def search_product(self, name):
        for prod in self.products:
            if prod.name == name:
                return prod
        return None

    def sort_products(self, criteria='name'):
        if criteria == 'name':
            self.products.sort(key=lambda x: x.name)
        elif criteria == 'category':
            self.products.sort(key=lambda x: x.category)
        elif criteria == 'quantity':
            self.products.sort(key=lambda x: x.quantity)
        elif criteria == 'price':
            self.products.sort(key=lambda x: x.price)
        else:
            print("Invalid sorting criteria.")

    def display_products(self):
        for prod in self.products:
            print(f"Name: {prod.name}, Category: {prod.category}, Quantity: {prod.quantity}, Price: {prod.price}")
