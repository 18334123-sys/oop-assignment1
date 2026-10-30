class Product:
    product_count = 0

    def __init__(self, name, sku, price, quantity):
        if not self.is_valid_sku(sku):
            raise ValueError("Invalid SKU")

        self.name = name
        self.sku = sku
        self.price = price
        self.quantity = quantity

        Product.product_count += 1

    def __repr__(self):
        return f"Product('{self.name}', '{self.sku}', {self.price}, {self.quantity})"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError("Price must be a number")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValueError("Quantity must be a non-negative integer")
        self._quantity = value

    @property
    def line_value(self):
        return self.price * self.quantity

    @property
    def is_low_stock(self):
        return self.quantity < 5

    @classmethod
    def from_csv_line(cls, line):
        name, sku, price, quantity = line.split(",")
        return cls(name, sku, float(price), int(quantity))

    @staticmethod
    def is_valid_sku(sku):
        return (
            len(sku) == 6
            and sku[:3].isalpha()
            and sku[3:].isdigit()
        )

    @classmethod
    def count(cls):
        return cls.product_count
