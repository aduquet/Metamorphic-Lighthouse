from get_info_class import GetInfoClass, getFunctionPath, getAllPathsNames, getFunctionCounterPerGroup
from save_files_class import SaveFiles
import pandas as pd
import numpy as np
import glob as gl
import pathlib
import time
import json
import sys
import os

def getFunctionsInfo(functionPath):
    
    functionPathsList = getFunctionPath(functionPath)  
    for functionPath in functionPathsList:
        auxList.append(getAllPathsNames(functionPath))
    
if __name__ == '__main__':
    
    import click
    
    global mainDF
    mainDF ={}
    
    global auxList
    auxList = []
    
    @click.command()
    @click.option('-i', '--root_path', 'root_path', help = 'Output file name')
    
    def main(root_path):
        
        mainPath = str(pathlib.Path().absolute()) + '/' + 'infoFile'
        
        try:
            os.mkdir(mainPath)
        
        except:
            pass
                
        groupName = GetInfoClass(root_path = root_path).getGroupName()
        groupsPaths = GetInfoClass(root_path=root_path).getGroupPaths()
        
        for g in groupsPaths:
            getFunctionsInfo(g)
        
        final_df = pd.DataFrame(auxList).sort_values(by=['groupID','functionName']).reset_index(drop=True)
        SaveFiles(final_df,'info_groups').saveCSV(True)
        print(getFunctionCounterPerGroup(final_df))
main()