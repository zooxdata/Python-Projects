#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:06:14 2021

@author: user
"""

"""

"""

RENTED = "rented.txt"
NOT_RENTED = "not_rented.txt"

class Rental:
    def __init__(self):
        # Using Dictionary to Tag the Fare
        self.carRate = {'Daily': 10, 'Weekly': 80, 'Weekends': 15}
        self.vanRate = {'Daily': 15, 'Weekly': 115, 'Weekends': 20}
        self.truckRate = {'Daily': 20, 'Weekly': 150, 'Weekends': 25}
     
    def displayRentalCost(self):
        ## using dictionary we can present the value of each type
        print("_______________________________________")
        print('|             Rental Rates             |')
        print("---------------------------------------")
        print("Daily: $",self.vehicleRate['Daily'])
        print("Weeekend: $", self.vehicleRate['Weekends'])
        print("Weekly: $", self.vehicleRate['Weekly'])
        
    def calculator(self):
        vehicleinput = input("#1 Car\n#2 Van\n#3 Truck\n.. ")
        ratetype = input("#1 Daily\n#2 Weekly\n#3 Weekends\n.. ")
        duration = input("Enter Duration of Rental: ")
        if vehicleinput == '1':
            vehicleRate = self.carRate
        elif vehicleinput == '2':
            vehicleRate = self.vanRate
        elif vehicleinput == '3':
            vehicleRate = self.truckRate
        else:
            print("Invalid input! Please try again.")
        if ratetype == '1':   
            rentaltotal = vehicleRate['Daily'] * int(duration)
        elif ratetype == '2':
            rentaltotal = vehicleRate['Weekly'] * int(duration)
        elif ratetype == '3':
            rentaltotal = vehicleRate['Weekend'] * int(duration) 
        else:
            print("\nInvalid input! Please try again.")
        print("\nTotal: $" + str(rentaltotal))
        
 
    def load_file(self,file):
    # '''
    # Load content of file. Parameter "file" includes path.
    # '''
        with open(file) as f:
            return f.read()

    
    def choose_vehicle(self):
    #User choose vehicle ID for rent.
    #The vehicle have to be in file of not rented vehicle.
    #If user choose invalid vin, prints out not available
        while True:

            VIN = input('Input the Identification Number of the vehicle you want to rent: ')
            print()
            if VIN.lower() =='q':
                return
            elif VIN in self.load_file(NOT_RENTED):
                return VIN
            else:
                if VIN in self.load_file(RENTED):
                    print('The vehicle is NOT available. Try again or press Q to go back.')
    
    def return_vehicle(self):
        while True:
            VIN = input('Input the Identification Number of the Vehicle you want to return: ')
            print()
            if VIN.lower() == 'q':
                return
            elif VIN in self.load_file(RENTED):
                return VIN
            else:
                print('Wrong choice, try again or press Q to go back.')
            
   
    def write_vehicle_to_file(self, vin, file):
        '''
        Write VIN to file.
        '''
        with open(file) as f:
            content = f.read()
            content = list(content.strip().replace('\n', ''))
            content.append(VIN)
            content.sort()
            content = '\n'.join(content)
        with open(file, 'w') as f:
            f.write(content)
        
    def del_vehicle_from_file(self, VIN, file):
        '''
        Delete VIN from file
        '''
        with open(file) as f:
            content = f.read()
            content = content.replace(VIN, '').replace('\n\n', '\n')
            with open(file, 'w') as f:
                f.write(content)
          
    def display(self):
        import pandas as pd
        if inventoryinput == '1':
            my_file =pd.read_csv('car_inventory_updated.csv', index_col='#')
        elif inventoryinput == '2':
            my_file =pd.read_csv('van_inventory_updated.csv', index_col='#')
        elif inventoryinput == '3':
            my_file =pd.read_csv('truck_inventory_updated.csv', index_col='#')
        else:
            print('Invalid input. Please try again.')
        print(my_file)
        
                
                   
   
rental = Rental()

while True:
    print("______________________________________")
    print('|        Vehicle Rental Agency        |')
    print("--------------------------------------")
    print("#1 View Vehicles: ")
    print("#2 View Rental Rates: ")
    print("#3 Rental Calculator: ")
    print("#4 Make A Reservation: ")
    print("#5 Cancel Reservation: ")
    print('#6 Quit')
    
    mainInput = input(".. ")
    
    if mainInput == '1':
        print("___________________________________")
        print('|         Type of Vehicles         |')
        print("-----------------------------------")
        print('#1 Car')
        print('#2 Van')
        print('#3 Truck')
        inventoryinput = input('.. ')
        print()
        rental.display() 

            
    elif mainInput == '2':
        print("___________________________________")
        print('|         Type of Vehicles         |')
        print("-----------------------------------")     
        print('#1 Car')
        print('#2 Van')
        print('#3 Truck')
        rentalcostinput = input(".. ")
        if rentalcostinput == '1':
            rental.vehicleRate = rental.carRate
        elif rentalcostinput == '2':
            rental.vehicleRate = rental.vanRate
        elif rentalcostinput == '3':
            rental.vehicleRate = rental.truckRate
        else: 
            print("Invalid input! Please try again.")
        rental.displayRentalCost()
            
    elif mainInput == '3':
        print("____________________________________")
        print('|         Rental Calculator         |')
        print("------------------------------------")
        rental.calculator()
        
        
    elif mainInput == '4':
        print("_______________________________")
        print('|         Reservations         |')
        print("-------------------------------")
        VIN = rental.choose_vehicle()
        if VIN:
            rental.write_vehicle_to_file(VIN, RENTED)
            rental.del_vehicle_from_file(VIN, NOT_RENTED)
            print('Booking Confirmd!')

    elif mainInput == '5':
        print("_______________________________")
        print('|         Reservations         |')
        print("-------------------------------")
        VIN = rental.return_vehicle()
        if VIN:
            rental.write_vehicle_to_file(VIN, NOT_RENTED)
            rental.del_vehicle_from_file(VIN, RENTED)
            print('Thank you, See you again!')
        
             
    elif mainInput == '6':
        raise SystemExit        
    
    else:
        print("\nInvalid input! Please try again!")
    