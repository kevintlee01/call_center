from Employee import Employee


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 2)
