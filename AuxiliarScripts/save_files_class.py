import os
import json
import pathlib
import pandas as pd

class SaveFiles():
    
    mainPath = None
    file_name_json = None
    file_name_csv = None
    
    def __init__(self, data: dict|list, file_name: str):

        self.data = data
        self.file_name_json = file_name + '.json'
        self.file_name_csv = file_name + '.csv'

        self.mainPath = str(pathlib.Path().absolute()) + '/infoFile'
        
        if os.path.exists(self.mainPath) == False:
            os.mkdir(self.mainPath)
        
    def saveJSON(self):

        filePath = self.mainPath + '/' + self.file_name_json
        with open(filePath, 'w') as file:
            json.dump(self.data, file)

    def saveCSV(self, index:bool):
        print(self.data)
        print(type(self.data))
        if isinstance(self.data, pd.DataFrame):
            print('****')
            self.data.to_csv(self.mainPath + '/' + self.file_name_csv, index = index)
            
        if isinstance(self.data, list):
            df = pd.DataFrame(self.data)
            df.to_csv(self.mainPath + '/' + self.file_name_csv, index = index)