from pizza_size import PizzaSize
from pizza import Pizza

# This function shows a limitation on tool-assisted
# refactoring in a dynamic language like Python.
#
# When you rename the Pizza getPrice method to get_price,
# does it rename the method here?
# - if no type annotation on the pizza parameter, maybe not
# - if use type annotation ':Pizza' on the parameter, it should


def print_pizza(pizza: Pizza):
    """
    Print a description of a pizza, along with its price.
    """
    # create printable description of the pizza such as
    # "small pizza with muschroom" or "small plain pizza"
    print(f"A {pizza}")
    print("Price:", pizza.get_price())


if __name__ == "__main__":
    pizza = Pizza(PizzaSize.jumbo)
    pizza.add_topping("mushroom")
    pizza.add_topping("tomato")
    pizza.add_topping("pineapple")
    print_pizza(pizza)

    pizza2 = Pizza(PizzaSize.medium)
    print_pizza(pizza2)

    pizza3 = Pizza(PizzaSize.large)
    pizza3.add_topping("seafood")
    print_pizza(pizza3)
