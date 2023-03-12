# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:43:51 2023

@author: kashf
"""

class Connection:
    """_summary_
    """

    def __init__(self,From_station,To_station,Color,Direction):
        self.dir=Direction
        self.fr_st=From_station
        self.to_st=To_station
        self.color=Color
        
        
        
    def __str__(self):
        return f"From str method of Test: Direction is {self.dir}, From_station is {self.fr_st}, To_station is {self.to_st}, Color is {self.color}"
    
    def __repr__(self):
        return f"From str method of Test: Direction is {self.dir}, From_station is {self.fr_st}, To_station is {self.to_st}, Color is {self.color}\n"
    