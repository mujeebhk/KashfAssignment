# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:33:49 2023

@author: kashf
"""

class Station:
    def __init__(self,Name,Delay_prob):
        self.name=Name
        self.delay_prob=Delay_prob
        
        
    def __str__(self):
        return f"From str method of Test: name is {self.name}, delay_prob is {self.delay_prob}"
    
    def __repr__(self):
        return f"From str method of Test: name is {self.name}, delay_prob is {self.delay_prob}"
    