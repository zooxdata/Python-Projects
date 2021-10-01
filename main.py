#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:45:40 2021

@author: user
"""

from Vehicles import Vehicle, Car, Van, Truck
from VehicleCost import VehicleCost, VehicleCosts
from Reservations import Reservation, Reservations

VEHICLE_TYPES = ('Car', 'Van', 'Truck')
VEHICLES_FILENAME = 'Car_Inventory.txt'
VEHICLES_COSTS_FILENAME = 'RentalCost.txt'

class Main:
    
    def __init__(self):
        self.__vehicle = Vehicle()
        self.__vehicle_costs = VehicleCosts()
        self.__reservations = Reservations()
        
        self.__vehicle_info_file = open(VEHICLES_FILENAME, 'r')
        self.__rental_cost_file = open(VEHICLES_COSTS_FILENAME, 'r')
        
    def numAvailVehicles(self, vehicle_type):
        return self.__vehicles.numAvailVehicles(vehicle_type)

    def getVehicle(self, vin):
        
        return self.__vehicles.getVehicle(vin)
    
    def getVehicleTypes(self):
        
        return VEHICLE_TYPES
    
    def getVehicleCosts(self, vehicle_type):
        return self.__vehicle_costs.getVehicleCost(vehicle_type).getCosts()
    
    def getAvailVehicles(self, vehicle_type):
        
        avail_vehicles = self.__vehicles.getAvailVehicles(vehicle_type)
        return [veh for veh in avail_vehicles]
    
    def isReserved(self, vin):
        return self.__reservations.isReserved(vin)
    
    def findReservation(self, mobile_number):
        
        return self.__reservations.findReservation(mobile_number)
    
    def addReservation(self, resv):
        
        self.__reservations.addReservation(resv)
        
    def cancelReservation(self, mobile_number):
        
        vin = self.__reservations.getVinForResv(mobile_number)
        self.__reservations.cancelReservation(mobile_number)
        self.__Inventory.unreserveVehicle(vin)
        
    def calcRentalCost(self, vehicle_type, rental_period):
        return self .__vehicle_costs.calcRentalCost(vehicle_type, rental_period)
    
    def __vehiclelist(self, vehicle_file):
        
        empty_str = ''
        
        vehicle_file_headers = ('#CARS#', '#VANS#', '#TRUCKS#')
        vehicle_type_index = 0
        
        vehicle_str = vehicle_file.readline()
        vehicle_info = vehicle_str.rstrip().split(',')
        file_header_found = vehicle_info[0]
        expected_header = vehicle_file_headers[0]
        
        if file_header_found == expected_header:
            
            vehicle_str = vehicle_file.readline()
            
            while vehicle_str != empty_str:
                
                vehicle_info = vehicle_str.rstrip().split(',')
                
                if vehicle_info[0][0] == '#':
                    vehicle_type_index = vehicle_type_index + 1
                    file_header_found = vehicle_info[0]
                    expected_header = vehicle_file_headers[vehicle_type_index]
                    
                else:
                    
                    if file_header_found == '#CARS#':
                        vehicle = Car(*vehicle_info)
                    elif file_header_found == '#TRUCK#':
                        vehicle = Truck(*vehicle_info)
                    elif file_header_found == '#VANS#':
                        vehicle = Van(*vehicle_info)
                        
                    self.__Inventory.addVehicle(vehicle)
                    
                vehicle_str = vehicle_file.readline()
                
Main.__vehiclelist()
                        
                        
        
        
    
print(VEHICLE_TYPES)
    
        