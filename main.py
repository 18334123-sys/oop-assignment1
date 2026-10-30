from inventory import Inventory
from product import Product


SAMPLE = [
    "Milk,MLK001,1.25,12",
    "Bread,BRD002,0.90,3",
    "Eggs,EGG003,2.40,30",
    "Coffee,COF004,7.50,2"
]


def main():
    inventory = Inventory.from_lines(SAMPLE)

    print("===== MiniMart Inventory Report =====")

    for product in inventory.products.values():
        print(
            f"{product.name}: "
            f"Price = {product.price:.2f}, "
            f"Quantity = {product.quantity}, "
            f"Line Value = {product.line_value:.2f}"
        )

    print("-------------------------------------")
    print(f"Total Inventory Value: {inventory.total_value():.2f}")

    print("\nLow Stock Products:")

    for product in inventory.products.values():
        if product.is_low_stock:
            print(product.name)

    print("-------------------------------------")
    print(f"Total Products Created: {Product.count()}")


if __name__ == "__main__":
    main()
