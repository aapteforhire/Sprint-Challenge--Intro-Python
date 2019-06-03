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
class Vehicle():
    '''This is the base class'''
    pass

class FlightVehicle(Vehicle):
    '''This class inherits from Vehicle'''
    pass

class Starship(FlightVehicle):
    '''This class inherits from FlightVehicle'''
    pass

class Airplane(FlightVehicle):
    '''This class inherits from FlightVehicle'''
    pass

class GroundVehicle(Vehicle):
    '''This class inherits from Vehicle'''
    pass

class Car(GroundVehicle):
    '''This class inherits from GroundVehicle'''
    pass

class Motorcycle(GroundVehicle):
    '''This class inherits from GroundVehicle'''
    pass