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
        
        random_connection=random.choice(connection_list)
        connection_list.remove(random_connection)
        print("Random track selected is ",random_connection)
        return random_connection
        #Select a random train station
        #Check the station of all other trains
        #If any other train is in the station already then loop back and select a random station again
        
        
    def simulate(stations,connections,trains):
        pass        
        
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
        
        
    no_of_trains=input("Enter how many trains to simulate:")
    #Loop to no_of_trains .. each time crate train object. 
    #Randomly select the station
    #Store in Trains List
    trains=[]
    temp_connections = connections
    for i in range (0, int(no_of_trains)):
        #tempTrain.number=i+1
        #Set Train stations
        temp_connection= Main.get_random_connection(temp_connections)
        tempTrain = Train(i+1, temp_connection.fr_st, temp_connection.dir, temp_connection.color)
        
        #tempTrain.cr_st =temp_connection.fr_st
        #tempTrain.cr_dir =temp_connection.dir
        trains.append(tempTrain)
    
    print(trains)

        
        
        
    
    
    
    while True:
        print("Continue simulation [1], train info [2], exit [q]")
        option=input("Select an option:")
        if option==1:
            
            #Invoke a method called simulate
            #Pass list of trains and list of stations  and list of tracks as parameter
            
            """delay=random.random()
            if delay==True:
                d[train].append("D")
            else:
                if d[train][1]==connections[random_train][1]:
                    train=[connections[random_train+1][2],connections[random_train+1][0],direction]
                """
                
                
                
        elif option==2:
            trainNumber=input("Which train (1 - 3):")
            #train_info(trains, trainNumber)
            
        elif option=='q' or option=='Q':
            break
        else:
            print("Invalid input")
            continue
        
        
        
    ''' 
                 
        def train_info(train):    
            direction=connections[random_train][-1]
            if direction=='S':
                direction=+'outh'
            else:
                direction+='orth'
            d[train] = [connections[random_train][2],connections[random_train][0],direction]
            print("Train ",train," on ",connections[random_train][2]," line is at station ",connections[random_train][0]," heading in ",direction," direction.")
            if d[train][-1]=='D:
                print("Delay")
                
    '''     



main()