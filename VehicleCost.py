#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:07:52 2021

@author: user
"""

class VehicleCost:
    
    def __init__(self, daily_rate, weekly_rate, weekend_rate):
        
        self.__daily_rate = daily_rate
        self.__weekly_rate = weekly_rate
        self.__weekend_rate = weekend_rate
        
    def getDailyRate(self):
        return float(self.__daily_rate)
    
    def getWeeklyRate(self):
        return float(self.__weekly_rate)
    
    def getWeekendRate(self):
        return float(self.__weekend_rate)
    
    def getCosts(self):
        return [self.__daily_rate, self.__weekly_rate, self.__weekend_rate]
    
# vc = VehicleCost('24.99', '180.00', '45.00')

# print(vc.getCosts())
# print(vc.getWeekendRate())


DAILY_RENTAL = 1
WEEKLY_RENTAL = 2
WEEKEND_RENTAL = 3

class VehicleCosts():
    
    def __init__(self):
        self.__vehicle_costs = dict()
        
    def getVehicleCost(self, vehicle_type):
        return self.__vehicle_costs[vehicle_type]
    
    def addVehicleCost(self, veh_type, veh_cost):
        self.__vehicle_costs[veh_type] = veh_cost
        
    def calcRentalCost(self, vehicle_type, rental_period):
        
        vehicle_cost = self.getVehicleCost(vehicle_type)
        
        rental_time = rental_period[1]
        
        if rental_period[0] == DAILY_RENTAL:
            rental_rate = vehicle_cost.getDailyRate()
            rental_period_value = DAILY_RENTAL
            rental_period_to_str = 'daily rental'
            rental_days = rental_time
            
        elif rental_period[0] == WEEKLY_RENTAL:
            rental_rate = vehicle_cost.getWeeklyRate()
            rental_period_value = WEEKLY_RENTAL
            rental_period_to_str = 'weekly rental'
            rental_days = rental_time * 7
            
        elif rental_period[0] == WEEKEND_RENTAL:
            rental_rate = vehicle_cost.getWeekendRate()
            rental_period_value = WEEKEND_RENTAL
            rental_period_to_str = 'weekend rental'
            rental_days = 2
        
        base_rental_charges = rental_days * rental_rate
            
        return 'base_rental_charges: ' + base_rental_charges

        
# vc_1 = VehicleCosts('24.99', '180.00', '45.0')
# vc_2 = VehicleCosts('35.00', '220.00', '45.0')
# vc.addVehicleCost('Car', vc_1)
# vc.addVehicleCost('Van', vc_2)

# vc.getVehicleCost('Car').getCosts()
# vc.calcRentalCost('Car', (1,3), False, 150)