# HW - 2 - Inhertiance - Medium to Hard - Package Delivery Service


class Address:
    def __init__(self, name, street, city):
        self.name = name
        self.street = street
        self.city = city

    def get_address(self):
        return f'Address of {self.name} is {self.street}, {self.city}'

class Package(Address):
    def __init__(self, sender_address, receiver_address, weight, price_per_kg):
        self.sender_address = sender_address 
        self.receiver_address = receiver_address  
        self.weight = max(weight, 0) 
        self.price_per_kg = max(price_per_kg, 0)

    def total_cost(self):
        return self.weight * self.price


class TwoDayPackage(Package):
    def __init__(self, sender_address, receiver_address, weight, price_per_kg, fixed_fee):
        super().__init__(sender_address, receiver_address, weight, price_per_kg)
        self.fixed_fee = max(fixed_fee, 0)

    def total_cost(self):
        return super().total_cost() + self.fixed_fee

class HeavyPackage(Package):
    def __init__(self, sender_address, receiver_address, weight, price_per_kg, extra_weight_price):
        super().__init__(sender_address, receiver_address, weight, price_per_kg)
        self.extra_weight_price = max(extra_weight_price, 0) 

    def total_cost(self):
        extra_fee = (self.weight - 100) * self.extra_weight_price if self.weight > 100 else 0
        return super().total_cost() + extra_fee




sender = Address('Ahmed', 'Downtown', 'Cairo')
receiver = Address('Mohamed', 'Downtown', 'Giza')

standard_package = Package(sender, receiver, 85, 20)
print("Standard Package Cost:", standard_package.total_cost())

two_day_package = TwoDayPackage(sender, receiver, 85, 20, 105)
print("Two-Day Package Cost:", two_day_package.total_cost())

heavy_package = HeavyPackage(sender, receiver, 150, 20, 10)
print("Heavy Package Cost:", heavy_package.total_cost())