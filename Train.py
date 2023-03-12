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
      return f"From str method of Test: Train {self.number}, on {self.line} line, is at station {self.cr_st}, heading in {self.cr_dir} direction"
  
    def __repr__(self):
      return f"From str method of Test: Train {self.number}, on {self.line} line, is at station {self.cr_st}, heading in {self.cr_dir} direction"
