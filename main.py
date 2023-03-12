# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:14:36 2023
Project Trains
@author: kashf
"""
#Importing all necessary class and standard libraries
from Station import Station
from Train import Train 
from Connection import Connection
import random
import copy

class Main:
    
    def load_stations(stations_file):
        """
        Loading data from the stations file into a list of objects      
        Args:
            stations_file (Text file): Contains the train stations and their probability of delay.
        """
        
        with open(stations_file,'r') as st:
            global stations #Making the variable global for enabling its use throughout the program
            stations=[]
            for i in st.readlines():
               split_list =  i.split(',')
               stations.append(Station(split_list[0], split_list[1])) #Appending objects to list
   
    
    def load_connections(connections_file):
        """
        Loading data from the stations file into a list of objects
        Args:
            connections_file (Text file): Conatains source station, target station, line and direction.
        """
        
        global connections #Making the variable global for enabling its use throughout the program
        connections=[]
        with open(connections_file,'r') as cn:
            for j in cn.readlines():
                split_list=j.split(',')

                #Removing the new-line character
                split_list[3]=split_list[3].strip() 

                #Appending existing connections from the file
                connections.append(Connection(split_list[0],split_list[1],split_list[2],split_list[3]))

                #Appending connections for opposite directions(for after train reaches final destination and has to change direction)
                connections.append(Connection(split_list[1],split_list[0],split_list[2],Main.opposite_of(split_list[3]))) 
        
            
    def opposite_of(direction):
        """
        Changing direction to opposite direction
        Args:
            direction (string): Current direction
        Returns:
            string: Opposite direction
        """

        new_direction=''
        if direction=='N' or direction=='N\n':
            new_direction='S'
        else:
            new_direction='N'
        return new_direction
               

    def get_random_connection(connection_list):
        """
        Choosing current position of train using random
        Args:
            connection_list (list): List of all connections
        Returns:
            list: Random connection chosen for position of train
        """
        
        #Making a copy of connections for further alterations
        connection_list_temp = copy.deepcopy(connection_list) 
        
        #Making the variable global for enabling its use throughout the program 
        global random_connection
        
        #Choosing a random connection from the list#
        random_connection=random.choice(connection_list_temp) 
        
        #Removing the above chosen connection to make sure no two trains are on the same randomly chosen position
        connection_list_temp.remove(random_connection) 
        
        return random_connection
        
        
    def findConnectionByTrain(train):
        """
        Finding the connection corresponding to the train
        Args:
            train (list): List of Objects of Train
        Returns:
            list: Entities of connection
        """
        
        for i in range (0, len(connections)):
            connection = connections[i]
            #Checking if the direction and station of the train and connection are same
            if (connection.dir == train.cr_dir and connection.fr_st==train.cr_st):
                return connection
         
        #Invoking the opposite_of function
        train.cr_dir = Main.opposite_of(train.cr_dir) 
        
        for i in range (0, len(connections)):
            connection = connections[i]
            #Checking if the station and opposite direction of the train and connection are same
            if (connection.dir == train.cr_dir and connection.fr_st==train.cr_st):
                return connection
           
               
    def findStationByName(name):
        """
        Finding the Station from the stations list  corresponding to the current station in train
        Args:
            name (string): Instance of Train
        Returns:
            list: List containing station name and delay probability
        """
       
        for i in stations:
            if i.name == name:
                return i
  
            
    def random_delay(probability):
        """ 
        Checking for delay with random and probabilty of delay for station
        Args:
            probability (float): Probabilty of delay of a station
        Returns:
            boolean: Returns whether delay occurs or not
        """
       
        return random.random() < probability  


    def simulate():
        """
        Changes the postiton of the given train according to its current position and delay probabilty
        """

        for i in range (0, len(trains)):
            tempTrain=trains[i]
            tempStation = Main.findStationByName(tempTrain.cr_st) #Invoking the method findStationByName
            connection = Main.findConnectionByTrain(tempTrain) #Invoking the method findConnectionByTrain
            
            #Taking the delay probability from Stations file according to station name 
            delay_prob=float(tempStation.delay_prob.strip())
            
            if Main.random_delay(delay_prob): #Invoking the random.delay function to check for delay
                print("Train delayed", tempTrain)
            else: 
                trains[i].cr_st = connection.to_st
                trains[i].cr_dir = connection.dir
                print(trains)
        
 
def main():
    """
        Starting point for Python to start execution of this program.
    """
      
    while True:
        stations_filename=input("Enter name of stations file:")
        try:
            Main.load_stations(stations_filename) #Invoking the load_stations method
            break
        except FileNotFoundError: #Error handling
            print("File Not Found--Please enter a valid file name")
            continue       
    while True:
        connections_filename=input("Enter name of connections file:")
        try:
            Main.load_connections(connections_filename) #Invoking the load_connections function
            break
        except FileNotFoundError: #Error handling
            print("File Not Found--Please enter a valid file name")
            break
        
    global no_of_trains #Making the variable global for enabling its use throughout the program
    no_of_trains=input("Enter how many trains to simulate:")   
    global trains #Making the variable global for enabling its use throughout the program
    trains=[]
    temp_connections = connections
    
    for i in range (0, int(no_of_trains)):
        temp_connection= Main.get_random_connection(temp_connections) #Invoking the get_random_connection function
        tempTrain = Train(i+1, temp_connection.fr_st, temp_connection.dir, temp_connection.color) #Creating a Train class object
        trains.append(tempTrain) #Appending the object into trains list 
        
    while True:
        print("Continue simulation [1], train info [2], route info [3], exit [q]")
        option=input("Select an option:")
        
        if option=='1':#Simulating 
            train_number=int(input("Which train:")) 
            Main.simulate() #Invoking the simulate method
            continue
        
        elif option=='2': #Displaying train information
            trainNumber=int(input("Which train:"))  
            print(trains[trainNumber-1]) #Printing the informstion for the train number entered
            continue 
        
        elif option=='3':
            start_station=input("Enter a start station")
            end_station=input("Enter an end station")
            time_steps=int(input("Enter time steps"))
           
        elif option=='q' or option=='Q': #--Exit--
            print("Thank you and Goodbye")
            break #Exiting the loop 
            
        else:
            print("Invalid input") #Error Handling
            continue


main()
