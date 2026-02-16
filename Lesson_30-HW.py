class Restaurant:
    def __init__(self, name, tables_count):
        self.name = name
        self.tables_count = tables_count
        self.reservations = {}

    def make_reservation(self, name, table_number, date):
        if date not in self.reservations:
            self.reservations[date] = 0

        if self.reservations[date] + table_number > self.tables_count:
            print("No seats available.")
        else:
            self.reservations[date] += table_number
            print(f"Reservation made for {name} at {date}.")

    def order_food(self, *items):
        print(f"Order with {', '.join(items)} placed!")


class FastFoodRestaurant(Restaurant):
    def __init__(self, name):
        super().__init__(name, 0)

    def make_reservation(self, name, table_number, date):
        print("We do not take reservations.")


restaurant = Restaurant('LavRestoran', 5)
restaurant.make_reservation('Anna', 2, '2024-05-06')

restaurant.make_reservation('Ashot', 3, '2024-05-07')
restaurant.make_reservation('Mary', 1, '2024-05-07')
restaurant.make_reservation('Lilit', 2, '2024-05-07')

fast_food = FastFoodRestaurant('Mak Donalce')
fast_food.make_reservation('Hayko', 2, '2023-10-24')
fast_food.order_food('Vazegn', 'Soda')
