# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Product import Product
from InventoryManagement import InventoryManagement


# Example usage:
if __name__ == "__main__":
    inventory = InventoryManagement()

    # Adding products
    inventory.add_product(Product("Apple", "Fruit", 50, 1.5))
    inventory.add_product(Product("Banana", "Fruit", 40, 1.0))
    inventory.add_product(Product("Milk", "Dairy", 20, 2.0))

    # Displaying products
    print("List of Products:")
    inventory.display_products()

    # Updating product quantity
    inventory.update_product("Apple", 45)
    print("\nAfter updating quantity of Apple:")
    inventory.display_products()

    # Removing a product
    inventory.remove_product("Banana")
    print("\nAfter removing Banana:")
    inventory.display_products()

    # Searching for a product
    searched_product = inventory.search_product("Milk")
    if searched_product:
        print(f"\nSearched Product: {searched_product.name}, Quantity: {searched_product.quantity}")
    else:
        print("Product not found.")

    # Sorting products by quantity
    print("\nProducts sorted by quantity:")
    inventory.sort_products('quantity')
    inventory.display_products()

