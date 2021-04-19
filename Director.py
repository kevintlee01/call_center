from Employee import Employee


class Director(Employee):
    def __init__(self, name):
        super().__init__(name, 1)
