#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: user
"""

from vehicles import Car
from vehicles import Van
from vehicles import Truck

class Inventory:
    def __init__(self):
        self.__vehicles = []
        ' This is to init and empty list of vehicles'
    
    def getVehicle(self, vin):
        
        for vehicle in self.__vehicles:
            if vehicle.getVin == vin:
                return vehicle
            
        ' Gives a Vehicle with the VIN as an identifier'
            
    def addVehicle(self, vehicle):
        ' Puts a vehicle into the list '    
        self.__vehicles.append(vehicle)
        
    def availableVehicles(self, get_type):
        'Returns vehicles that are available'
        return [veh for veh in self.__vehicles \
                if veh.get_type() == get_type and not veh.reserved]
            
    def unreserveVehicle(self, vin):
        
        x = 0
        found = False
        
        while not found:
            if self.__vehicles[x].getVin() == vin:
                self.__vehicles[x].reserved(False)
                found = True
                
# ### TEST CASES TO SEE IF THEY WORK
# veh_1 = Car('Chevrolet', '4', '4', '30', 'SIJDSID93893')
# veh_2 = Van('Defender', '4', '34', 'SDJIDJS0303')
# veh_3 = Truck('4', '40', '39', 'SJDKSDJ3939')

# i = Inventory()
# i.addVehicle(veh_1)
# i.addVehicle(veh_2)
# i.addVehicle(veh_3)

# print(i.availableVehicles('Car')[0].get_description())
# print(i.availableVehicles('Van')[0].get_description())
# print(i.availableVehicles('Truck')[0].get_description())

        
