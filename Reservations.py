#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:29:34 2021

@author: user
"""

class Reservation:
    def __init__(self, name, mobile_number, vin):
        
        self.__name = name
        self.__mobile_number = mobile_number
        self.__vin = vin
        
    def getName(self):
        return self.__name
    
    
    def getMobileNumber(self):
        
        return self.__mobile_number
    
    
    def getVin(self):
        return self.__vin

class Reservations:
    
    def __init__(self):
        ' Initiates an empty reservation'
        
        self.__reservations = dict()
        
    def isReserved(self, vin):
        ' returns True if reservation for vin, else returns False'
        return vin in self.__reservations
    
    def getVinForReserv(self, credit_card):
        ' returns vin of vehicles reserved with credit_card'
        
        return self.__reservations[credit_card].getVin()
    
    def addReservations(self, resv):
        ' add a new reservation'
        
        self.__reservations[resv.getMobileNumber()] = resv
        
    def FindReservations(self, mobile_number):
        
        return mobile_number in self.__reservations
    
    def cancelReservation(self, mobile_number):
        
        del(self.__reservations[mobile_number])