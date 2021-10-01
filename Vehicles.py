#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: user
"""

class Vehicle:
    def __init__(self, mpg, vin):
        # Miles Per Gallon
        self._mpg = mpg
        # Vehicle Indentification Number
        self._vin = vin
        # Reservation Status
        self._reserved = False
        
    @property
    def vin(self):
        return self._vin
    
    @property
    def reserved(self):
        return self._reserved
    
    @reserved.setter
    def reserved(self, reserved):
        if isinstance(reserved, bool):
            self._reserved = reserved
            
    def get_type(self):
        if isinstance(self, Car):
            return 'Car'
        elif isinstance(self, Van):
            return 'Van'
        elif isinstance(self, Truck):
            return 'Truck'
        
    def get_description(self):
        return "MPG: {} VIN: {}".format(self._mpg, self.vin)
          

class Car(Vehicle):
    def __init__(self, make_model, passengers, doors, mpg, vin):
        super().__init__(mpg, vin)
        self._make_model = make_model
        self._passengers = passengers
        self._doors = doors
        
    def get_description(self):
        return "  CAR MODEL: {} PASSENGERS: {} DOORS: {} ".format(self._make_model, self._passengers, self._doors) + super().get_description()
        
        
        
class Van(Vehicle):
    def __init__(self, make_model, passengers, mpg, vin):
        super().__init__(mpg, vin)
        self._make_model = make_model
        self._passengers = passengers
        
    def get_description(self):
        return "  CAR MODEL: {} PASSENGERS: {} ".format(self._make_model, self._passengers) + super().get_description()
        
        
class Truck(Vehicle):
    def __init__(self, rooms, length, mpg, vin):
        super().__init__(mpg, vin)
        self._length = length
        self._rooms = rooms
        
    def get_description(self):
        return "  LENGTHS: {} ROOMS: {} ".format(self._length, self._rooms) + super().get_description()



        