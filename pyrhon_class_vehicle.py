class Vehicle:
    def drive_forward(self):
        print("Yes, I do drive forward")

    def drive_backward(self):
        print("Yes, I do drive backward")

class Car(Vehicle):
    def __init__(self,cylinder):
        self.cylinder=cylinder

    def engine(self):
        print("I have {} cylinder engine".format(self.cylinder))
class Truck(Car):
    def __init__(self,cylinder):
        Car.__init__(self,cylinder)
        print("hello")

truck1=Truck(8)
truck1.engine()
truck1.drive_forward()
truck1.drive_backward()
car1=Car(4)
car1.drive_backward()
car1.drive_forward()
car1.engine()