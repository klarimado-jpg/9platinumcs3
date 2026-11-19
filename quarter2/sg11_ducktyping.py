class Car:
  def move(self):
    print ("The car drives on the road.")

class Boat:
  def move(self):
    print ("The boat sails on water.")

class Drone:
  def move(self):
    print("The drone flies in the sky.")

def start_trip(vehicle):
  vehicle.move()

car = Car()
boat = Boat()
drone = Drone()

start_trip(car)
start_trip(boat)
start_trip(drone)


Questions:

1. What is ducktyping as explained in the video? 
- Duck typing means a function or code cares about what an object can do or the methods and behaviors it has, not what type or what class it is. 

2. What did the car class need to have so it could work inside the same loop as dog and cat, even if it does not inherit from the class animal?
- The car class needs to have the same method that the dog and cat classes also have so that it could perform the action or the code. 
