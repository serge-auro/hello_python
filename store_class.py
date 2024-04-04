# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача — создать класс `Store`, который можно будет использовать для создания различных магазинов.
# Шаги:
# 1. Создай класс `Store`:
# -Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
# - Методы класса:
# - `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
# -  метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
# - метод для обновления цены товара.
# 2. Создай несколько объектов класса `Store`:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, item_price):
        self.items[item_name] = item_price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

# Creating instances of the Store class
store1 = Store("Grocery Store", "123 Main St")
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)
store1.add_item("lemons", 1.15)

store2 = Store("Hardware Store", "456 Oak St")
store2.add_item("hammer", 10)
store2.add_item("screwdriver", 5)

store3 = Store("Bookstore", "789 Elm St")
store3.add_item("fiction book", 15)
store3.add_item("non-fiction book", 20)

# Testing methods of one store
print(store1.get_price("apples"))

store1.update_price("apples", 1.1)
print(store1.get_price("apples"))

store1.remove_item("bananas")
print(store1.get_price("bananas")) 
