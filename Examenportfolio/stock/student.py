class Part:
        def __init__(self, name, price):
            self.name=name
            self.price=price
            self.quantity=0

        def get_quantity(self):
            return self.quantity
        
        def set_quantity(self, amount):
            if amount < 0:
                raise ValueError("Cant have negative parts")
            self.quantity=amount

        def __repr__(self):
            return (
                f"(Part: name = {self.name}, "
                f"price = {self.price}, "
                f"quantity = {self.quantity})"
            )
        

class Stock:
        def __init__(self):
            self.parts_dict = {}

        def add_part(self,name,price,quantity):
            if name in self.parts_dict:
                raise ValueError(f"Part with name {name} already in list")
            new_part = Part(name,price)
            new_part.set_quantity(quantity)
            self.parts_dict[name] = new_part

        def get_parts(self):
            return list(self.parts_dict.values())

        def remove_part(self, name):
            if name in self.parts_dict:
                del self.parts_dict[name]
            else:
                raise ValueError(f"{name} Is not an item in stock")

        def restock_part(self, name, amount):
            if amount < 0:
                raise ValueError("Cannot restock a negative amount")
        
            if name not in self.parts_dict:
                raise ValueError("Cant add stock to parts not in stock")
            
            part = self.parts_dict[name]
            part.quantity += amount


class Shop:
        def __init__(self, name):
            self.name=name
            self.__stock = Stock() 

        def get_stock(self):
            return self.__stock

        def load_stock_from_file(self, filename):
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    parts = line.split("|")
                    name = parts[0]
                    price = float(parts[1])
                    quantity = int(parts[2])
                    self.__stock.add_part(name,price,quantity)

        def save_stock_to_file(self, filename):
            with open(filename, "w", encoding="utf-8") as file:
                for part in self.__stock.get_parts():  #for every part in the list
                    line = f"{part.name} | {part.price} | {part.quantity}\n"
                    file.write(line)

        def display_stock(self):
            parts = self.__stock.get_parts()
            print("Current stock is:")
            for part in parts:             #":.2f" makes sure the price has 2 after decimal
                print(f"{part.name}: Price = {part.price:.2f}, Available Quantity = {part.quantity}")
            return parts
        
        def register_sale(self, name, quantity):
            stock = self.__stock

            if name not in stock.parts_dict:
                raise ValueError(f"No more {name}'s in stock")

            part = stock.parts_dict[name]

            if quantity > part.quantity:
                raise ValueError(f"Not enough in stock, only {part.quantity} left in stock")

            part.quantity -= quantity

            self.write_sale("Examenportfolio\\stock\\sales.txt", part.name, part.price, quantity)

            if part.quantity == 0:
                stock.remove_part(name)

        def write_sale(self, filename, name, price, quantity):
            # "a" mode = append to the file
            with open(filename, "a", encoding="utf-8") as file:
                file.write(f"Sold {quantity} item(s) from product {name} for price {price:.2f}\n")


                
def display_menu():
        print("\n===== IT Store Stock Management System =====")
        print("1. Add new part")
        print("2. Restock existing part")
        print("3. Sell part")
        print("4. View stock")
        print("5. Remove existing part")
        print("6. Exit")
        choice = input("Enter your choice: ")
        return choice

def main():
        shop = Shop("The IT Store")
        
        # Load existing stock if file exists
        try:
            shop.load_stock_from_file("Examenportfolio\\stock\\stock.txt")
        except FileNotFoundError:
            print("No stock file found. Starting with empty stock.")
        
        stop = False
        while not stop:
            choice = display_menu()

            if choice == '1':
                # Add new part
                name = input("What is the name of the part?: ")
                price = float(input("What is the price of the part?: "))
                quantity = int(input("How many do you wish to add?: "))
                shop.get_stock().add_part(name, price, quantity)
                print(f"{name} added to stock.")

            elif choice == '2':
                # Restock existing part
                name = input("Which part do you want to restock?: ")
                quantity = int(input("How many units to add?: "))
                try:
                    shop.get_stock().restock_part(name, quantity)
                    print(f"{quantity} units added to {name}.")
                except ValueError as e:
                    print(e)

            elif choice == '3':
                # Register sale
                name = input("Which part was sold?: ")
                quantity = int(input("How many units were sold?: "))
                try:
                    shop.register_sale(name, quantity)
                    print(f"Sold {quantity} units of {name}.")
                except ValueError as e:
                    print(e)

            elif choice == '4':
                # Display stock
                shop.display_stock()

            elif choice == '5':
                # Remove part
                name = input("Which part do you want to remove?: ")
                try:
                    shop.get_stock().remove_part(name)
                    print(f"{name} removed from stock.")
                except ValueError as e:
                    print(e)

            elif choice == '6':
                # Stop and save
                shop.save_stock_to_file("Examenportfolio\\stock\\stock.txt")
                print("Stock saved. Exiting.")
                stop = True

            else:
                print("Invalid choice. Please try again.")

# Run the program
main()
