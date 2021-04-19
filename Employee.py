class Employee:
    def __init__(self, name, rank):
        self.name = name
        self.free = True
        self.rank = rank

    def getName(self):
        return self.name

    def isFree(self):
        return self.free

    def receiveCall(self):
        self.free = False

    def endCall(self):
        self.free = True

    def getRank(self):
        return self.rank
