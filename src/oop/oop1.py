# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#base class / parent
class Vehicle:
    pass

# child
class FlightVehicle(Vehicle):
    pass

# grandChild
class Starship(FlightVehicle):
    pass

# grandChild
class Airplane(FlightVehicle):
    pass

# child
class GroundVehicle(Vehicle):
    pass

# grandChild
class Car(GroundVehicle):
    pass

# grandChild
class Motorcycle(GroundVehicle):
    pass
