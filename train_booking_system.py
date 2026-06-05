from random import randint, choice

class Train:
    def __init__(self, trainNO):
        self.trainNO = trainNO

    def book(self, fro, to):
        print(f"Ticket is booked in train no {self.trainNO} from {fro} to {to}\n")

    def getstatus(self):
        print(f"Train no {self.trainNO} is running on time\n")

    def getfare(self, fro, to):
        print(f"Ticket fare in train no {self.trainNO} from {fro} to {to} is ${randint(10, 80)}\n")

    def gettime(self):
        times = ["06:00 AM", "09:30 AM", "01:15 PM", "04:45 PM", "08:20 PM\n"]
        time = choice(times)
        print(f"Departure time: {time}")
fro = input("Enter departure city: ")
to = input("Enter destination city: ")


t = Train(randint(100000, 999999))

t.book(fro, to)
t.gettime()
t.getstatus()
t.getfare(fro, to)