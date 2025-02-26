# Hw - 1 - Inheritance - Medium to Hard - IKea’s Items

class simple_Ikea_item:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def get_salary(self):
        return self.salary


class complex_Ikea_item(simple_Ikea_item):
    total_s = 0
    def __init__(self, name, id, items, color=None):
        super().__init__(name, id, 0)
        self.items = items
        self.color = color

    def get_salary(self):
        return sum(item.get_salary() for item in self.items) 



left_leg = simple_Ikea_item('left_leg', 1, 65)
right_leg_base = simple_Ikea_item('right_leg_base', 2, 30)
extension = simple_Ikea_item('extension', 3, 70)
right_leg = complex_Ikea_item('right_leg', 4, [right_leg_base, extension])

special_chair = complex_Ikea_item('special_chair', 5, [left_leg, left_leg, right_leg], color='red')

print(f"Total price of the {special_chair.name}: ${special_chair.get_salary()}")


