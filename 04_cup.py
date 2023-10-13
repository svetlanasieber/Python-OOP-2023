class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity):
        free_space = self.size - self.quantity
        if free_space >= quantity:
            self.quantity += quantity
        else:
            self.quantity = self.size

    def status(self):
        return self.size - self.quantity


# Example usage
cup = Cup(100, 50)
print(cup.status())  # Output should be 50
cup.fill(40)  # The cup now has 90 units of liquid
cup.fill(20)  # The cup can only be filled up to 100, so it now has 100 units of liquid
print(cup.status())  # Output should be 10