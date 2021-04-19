from Respondent import Respondent
from Manager import Manager
from Director import Director

class CallRoute:
    def __init__(self, respondentCount, managerCount, directorCount):
        self.respondentStack = []
        self.managerStack = []
        self.directorStack = []
        self.calls = []
        self.initializeEmployees(respondentCount, managerCount, directorCount)

    def initializeEmployees(self, respondentCount, managerCount, directorCount):
        for i in range(respondentCount):
            self.respondentStack.append(Respondent("Respondent"+str(i)))

        for i in range(managerCount):
            self.managerStack.append(Manager("Manager"+str(i)))

        for i in range(directorCount):
            self.directorStack.append(Director("Director"+str(i)))

    def receiveCall(self):
        if len(self.respondentStack) > 0:
            respondent = self.respondentStack.pop()
            respondent.receiveCall()
            self.calls.append(respondent)
        else:
            print("No respondents available!")

    def escalateCall(self, callNumber):
        callNumber += 1

        if callNumber < len(self.calls):
            currentRank = self.calls[callNumber].getRank()
            current = self.calls[callNumber]
            escalated = None

            if currentRank == 1 and len(self.managerStack) > 0:
                print("Call {} Escalated to Manager!".format(callNumber))
                escalated = self.managerStack.pop()
            elif len(self.directorStack) > 0:
                print("Call {} Escalated to Director!".format(callNumber))
                escalated = self.directorStack.pop()
            else:
                print("Call {} Cannot be Escalated".format(callNumber))
                escalated = current

            escalatedRank = escalated.getRank()

            if currentRank != escalatedRank:
                current.endCall()
                escalated.receiveCall()

                if currentRank == 1:
                    self.respondentStack.append(current)
                if currentRank == 2:
                    self.managerStack.append(current)

                self.calls[callNumber] = escalated
        else:
            print("Call number not found!")

    def printCallCenter(self):
        print("\nRespondents Available")
        if len(self.respondentStack) > 0:
            for i in range(len(self.respondentStack)):
                print(self.respondentStack[i].getName())
        else:
            print("No Respondents Available")

        print("\nManagers Available")
        if len(self.managerStack) > 0:
            for i in range(len(self.managerStack)):
                print(self.managerStack[i].getName())
        else:
            print("No Managers Available")

        print("\nDirectors Available")
        if len(self.directorStack) > 0:
            for i in range(len(self.directorStack)):
                print(self.directorStack[i].getName())
        else:
            print("No Directors Available")

        print("\nPeople on Call")
        if len(self.calls) > 0:
            for i in range(len(self.calls)):
                print(self.calls[i].getName())
        else:
            print("No One On Call")


if __name__ == "__main__":
    callCenter = CallRoute(6, 2, 1)
    callCenter.receiveCall()
    callCenter.receiveCall()
    callCenter.receiveCall()
    callCenter.receiveCall()
    callCenter.escalateCall(1)
    callCenter.escalateCall(2)
    callCenter.escalateCall(2)
    callCenter.printCallCenter()
