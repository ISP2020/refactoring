from enum import Enum


class PizzaSize(Enum):
    # Enum members written as: name = value
    small = {'base': 120, 'topping': 20}
    medium = {'base': 180, 'topping': 25}
    large = {'base': 280, 'topping': 30}
    jumbo = {"base": 500, "topping": 50}

    def __str__(self):
        return self.name

    def price(self, ntoppings=0):
        return self.value['base'] + self.value['topping']*ntoppings


# def test_pizza_sizes():
#     for size in PizzaSize:
#         print(size.name, "pizza price:", size.value)
#
#
# if __name__ == "__main__":
#     test_pizza_sizes()
