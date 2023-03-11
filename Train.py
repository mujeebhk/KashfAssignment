# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:41:36 2023

@author: kashf
"""

class Train:
    def __init__(self,number,current_station,current_direction,line):
        self.number=number
        self.cr_st=current_station
        self.cr_dir=current_direction
        self.line=line
        

    def __str__(self):
        return f"Train: name is {self.number},  Current Station is  {self.cr_st}, direction is  {self.cr_dir}, line is  {self.line}"
    
    def __repr__(self):
        return f"Train: name is {self.number},  Current Station is  {self.cr_st}, direction is  {self.cr_dir}, line is  {self.line}"
    