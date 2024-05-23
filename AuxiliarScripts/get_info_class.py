import math
import traceback
import glob as gl
import pandas as pd

def getFunctionPath(groupPath):
    groupPath = groupPath + '/*'
    return gl.glob(groupPath)

def getAllPathsNames(functionPath):
    
    mainFunctionPath = functionPath.split('/')
    pythonFileName = mainFunctionPath[-1]
    
    return {
        'groupID' : mainFunctionPath[-2],
        'fullPathToFunctionDir': functionPath,
        'fullPathToFunctionSrcDir': functionPath + '/scr',
        'fullPathToFunctionTestDir': functionPath + '/test',
        'fullPathToFunctionPYfile': functionPath + '/scr/' + pythonFileName + '.py',
        'functionName': pythonFileName
        }

def getFunctionCounterPerGroup(df):
    return df['groupID'].value_counts()
    
class GetInfoClass():
    
    def __init__(self, root_path:str):
        self.root_path =root_path
        
    def getGroupName(self):
        
        path_splited = self.root_path.split('/')
        
        if path_splited[-1] != '*':
            groupsList = gl.glob(self.root_path+'/*')       
        else:
            groupsList= gl.glob(self.root_path)
            
        groupName = []
        
        for g in groupsList:
            groupName.append(g.split('/')[-1])  
        return groupName
        
    def getGroupPaths(self):
        
        path_splited = self.root_path.split('/')
        
        if path_splited[-1] != '*':
            groupsList = gl.glob(self.root_path+'/*')
        else:
            groupsList= gl.glob(self.root_path)
            
        return groupsList
    

        
        
    



        
        