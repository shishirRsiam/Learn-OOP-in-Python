class Car():
    color = "black"
    def start(self):
        print("Car Started...")
    @staticmethod
    def stop():
        print("Car Stoped!!!")
class mercities(Car):
    def __init__(self, name):
        self.name = name
        self.price = "1 Coror"

car1 = mercities("Bence")

print(car1.color, car1.name)
car1.start()
car1.stop()