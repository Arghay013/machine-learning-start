from abc import ABC, abstractmethod

# Abstract base class
class RestaurantSystem(ABC):
    @abstractmethod
    def show_menu(self):
        pass

    @abstractmethod
    def take_order(self):
        pass

    @abstractmethod
    def show_bill(self):
        pass


# Class for menu items
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Concrete class inheriting from RestaurantSystem
class Restaurant(RestaurantSystem):
    def __init__(self, name):
        self.name = name
        self.menu = []
        self.order = []

    def add_menu_item(self, item):
        self.menu.append(item)

    # Implement abstract methods
    def show_menu(self):
        print(f"\n🍽️ Welcome to {self.name} Menu:")
        for i, item in enumerate(self.menu, start=1):
            print(f"{i}. {item.name} - ${item.price}")
        print()

    def take_order(self):
        self.show_menu()
        while True:
            choice = input("Enter item number to order or 'done' to finish: ")
            if choice.lower() == 'done':
                break
            if choice.isdigit() and 1 <= int(choice) <= len(self.menu):
                selected_item = self.menu[int(choice) - 1]
                self.order.append(selected_item)
                print(f"✅ Added {selected_item.name} to your order.")
            else:
                print("❌ Invalid choice, please try again.")

    def show_bill(self):
        print("\n🧾 Your Bill:")
        total = 0
        for item in self.order:
            print(f"- {item.name}: ${item.price}")
            total += item.price
        print(f"\nTotal Amount: ${total}")
        print("Thank you for dining with us! 🍴")


# ---- Main Program ----
restaurant = Restaurant("Tasty Bites")

# Add some menu items
restaurant.add_menu_item(MenuItem("Burger", 5))
restaurant.add_menu_item(MenuItem("Pizza", 8))
restaurant.add_menu_item(MenuItem("Pasta", 7))
restaurant.add_menu_item(MenuItem("Coffee", 3))

# Run the program
restaurant.take_order()
restaurant.show_bill()
