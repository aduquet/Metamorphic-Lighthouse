from pathlib import Path
import pandas as pd

class GetViolationsNoViolations():
    
    def __init__(self, data, key_name):
        self.data = data
        self.key_name = key_name
        self.cntV = 0
        self.cntNV = 0
        self.cntE = 0
    
    def getViolations(self):
        
        cnt_violations = 0
        
        for key, value in self.data.items():
            
            if value[self.key_name] == 'Violate' or value[self.key_name] == 'violate':
                cnt_violations += 1
            
        avg = round((cnt_violations/len(self.data))*100)
        
        self.cntV = cnt_violations
        
        return avg
    
    def getViolations_cnt(self):
        return self.cntV
    
    def getNoViolations(self):
        
        cnt_Nviolations = 0
        
        for key, value in self.data.items():
            
            if value[self.key_name] == 'No-violate' or value[self.key_name] == 'no-violate':
                cnt_Nviolations += 1
            
        avg = round((cnt_Nviolations/len(self.data))*100) 
        
        self.cntNV = cnt_Nviolations
        
        return avg
    
    def getNoViolations_cnt(self):
        return self.cntNV
    
    def getExceptions(self):
        
        cnt_otros = 0
        
        for key, value in self.data.items():
            
            if value[self.key_name] == 'error' or value[self.key_name] == 'error':
                cnt_otros += 1
            
        avg = round((cnt_otros/len(self.data))*100)
        
        self.cntE = cnt_otros
        return avg      
    
    def getError_cnt(self):
        return self.cntE