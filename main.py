# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:14:36 2023
Project Trains
@author: kashf
"""
from Station import Station
from Train import Train 
from Connection import Connection
import random
import copy

class Main:
    
    
    def load_stations(stations_file):
        with open(stations_file,'r') as st:
            global stations
            stations=[]
            for i in st.readlines():
               split_list =  i.split(',')
               stations.append(Station(split_list[0], split_list[1]))
            print (str(x) for x in stations)
            print(stations)
   
    def load_connections(connections_file):
        global connections
        with open(connections_file,'r') as cn:
            connections=[]
            for j in cn.readlines():
                split_list=j.split(',')
                print(split_list)
                split_list[3]=split_list[3].strip()
                connections.append(Connection(split_list[0],split_list[1],split_list[2],split_list[3]))
                connections.append(Connection(split_list[1],split_list[0],split_list[2],Main.opposite_of(split_list[3])))
                print(len(connections))
            print("test")
            print(connections)
                
    def opposite_of(direction):
        new_direction=''
        if direction=='N' or direction=='N\n':
            new_direction='S'
        else:
            new_direction='N'
        return new_direction
               
    """def read_map():
        for i in connections:
            pass
"""
    def get_random_connection(connection_list):
        connection_list_temp = copy.deepcopy(connection_list)
        global random_connection
        random_connection=random.choice(connection_list_temp)
        connection_list_temp.remove(random_connection)
        print("Random track selected is ",random_connection)
        return random_connection
        #Select a random train station
        #Check the station of all other trains
        #If any other train is in the station already then loop back and select a random station again
        
    def findConnectionByTrain(train):
        for i in range (0, len(connections)):
            connection = connections[i]
            #print(connection)
            if (connection.dir == train.cr_dir and connection.fr_st==train.cr_st):
                #print(connection)
                return connection

        train.cr_dir = Main.opposite_of(train.cr_dir)
        for i in range (0, len(connections)):
            connection = connections[i]
            #print(connection)
            if (connection.dir == train.cr_dir and connection.fr_st==train.cr_st):
                #print(connection)
                return connection
           
        
        
    def findStationByName(name):
        for i in stations:
            if i.name == name:
                return i


    def simulate():
        for i in range (0, len(trains)):
            tempTrain=trains[i]
            tempStation = Main.findStationByName(tempTrain.cr_st)
            connection = Main.findConnectionByTrain(tempTrain)
            if connection == None:
                print("Connection not found for train : " , tempTrain)
                print("List of connections are  : " , connections)
                
            delay_prob=float(tempStation.delay_prob.strip())
            
            if Main.random_delay(delay_prob):
                print("Train delayed", tempTrain)
            else: 
                trains[i].cr_st = connection.to_st
                trains[i].cr_dir = connection.dir
            #print(connection)
        print(trains)
 
    def random_delay(probability):
      return random.random() < probability  

             
        
def main():
    d={}
    while True:
        #stations_filename=input("Enter name of stations file:")
        stations_filename="stations.txt"
        try:
            Main.load_stations(stations_filename)
            break
        except:
            print("Invalid input--File Not Found")
            continue
        
    while True:
       # connections_filename=input("Enter name of connections file:")
        connections_filename="connections.txt"
        try:
            Main.load_connections(connections_filename)
            break
        except:
            print("Invalid Error--File Not Found" +connections_filename)
            break
        
        
    #no_of_trains=input("Enter how many trains to simulate:")
    no_of_trains=3
    global trains
    trains=[]
    temp_connections = connections
    for i in range (0, int(no_of_trains)):
        #tempTrain.number=i+1
        #Set Train stations
        temp_connection= Main.get_random_connection(temp_connections)
        tempTrain = Train(i+1, temp_connection.fr_st, temp_connection.dir, temp_connection.color)
        
        #tempTrain.cr_st =temp_connection.fr_st
        #tempTrain.cr_dir =temp_connection.dir
        print("Connection assigned to ", tempTrain)
        trains.append(tempTrain)
    
    print(trains)
    
    while True:
        print("Continue simulation [1], train info [2], exit [q]")
        option=input("Select an option:")
        if option=='1':
            #train_number=int(input("Which train (1-",no_of_trains))
            train_number=1

            Main.simulate()
            continue
            
           #Invoke a method called simulate
           #Pass list of trains and list of stations  and list of tracks as parameter     
                
                
        elif option=='2':
            trainNumber=int(input("Which train (1 - 3):"))
            print(trains[trainNumber-1])
            continue
            
        elif option=='q' or option=='Q':
            print("Thank you and Goodbye")
            break
        else:
            print("Invalid input")
            continue


main()
