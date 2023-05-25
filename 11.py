def pr1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название ресторана: {self.restaurant_name}, кухня: {self.cuisine_type} итальянская')

        def open_restoraunrt(self):
            print('Ресторан сейчас открыт')

    new_Restaurant = Restaurant('PIZZALINO', '')
    print(new_Restaurant.restaurant_name)
    print(new_Restaurant.cuisine_type)

    new_Restaurant.describe_restaurant()
    new_Restaurant.open_restoraunrt()


def pr2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название ресторана: {self.restaurant_name}, кухня: {self.cuisine_type}')

        def open_restoraunrt(self):
            print('Ресторан сейчас открыт')

    new_Restaurant = Restaurant('Koreana', 'корейская')

    new_Restaurant2 = Restaurant('Peperio', 'итальянская')

    new_Restaurant3 = Restaurant('DUMICH', 'немецкая')

    new_Restaurant.describe_restaurant()
    new_Restaurant2.describe_restaurant()
    new_Restaurant3.describe_restaurant()


def pr3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating_restaurant):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating_restaurant = rating_restaurant

        def describe_restaurant(self):
            print(
                f'Название ресторана: {self.restaurant_name}, кухня: {self.cuisine_type} итальянская, рейтинг ресторана: {self.rating_restaurant}')

        def open_restoraunrt(self):
            print('Ресторан сейчас открыт')

        def rrating_restaurant(self):
            print(f'Новый рейтинг ресторана: {input("Введите новый рейтинг: ")}')

    new_Restaurant = Restaurant('PIZZALINO', '', 4)

    new_Restaurant.describe_restaurant()
    new_Restaurant.open_restoraunrt()
    new_Restaurant.rrating_restaurant()


pr1(), pr2(), pr3()
