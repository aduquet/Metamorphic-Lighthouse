from rule_mining_module import RuleMiningModule
from feature_extractor import FeatureExtractor
from AuxUtility import Utility
import pandas as pd
import glob as gl
import pathlib
import json
import os

def process(tarjet_path, output_path):
    
    file_name = Utility.getName(tarjet_path)
    
    if (Utility.is_json_file(fileNme=file_name)):
        auxList = []
        
        with open(tarjet_path, 'r') as file:
            data = json.load(file)
            
        for key, values in data.items():
            
            new_features = FeatureExtractor(instance= values, key= key).new_dataset()
            auxList.append(new_features)
            
        df = pd.DataFrame(auxList)
        
        df.to_csv(output_path)   
    
    else:
        raise ValueError("Error with processing the file, be sure to be a json file")

    return df

def start_rule_mining(data, path_store):
    rm = RuleMiningModule(data=data, support=0.5, conf=1)
    df_encode = rm.enconde()
    df_unique_encode = df_encode.drop_duplicates()
    
    k = df_unique_encode.keys()    
    # Filter columns containing '_NA' in their names
    columns_to_drop = [col for col in df_unique_encode.columns if '_NA' in col]

    # Drop filtered columns
    df_unique_encode = df_unique_encode.drop(columns=columns_to_drop)
    
    if 'vs_str_error' in k:
        rm.ruleGenerator_e(df_encode=df_unique_encode, path_store=path_store)
    
    if 'vs_str_No-violate' in k:
        rm.ruleGenerator_nv(df_encode=df_unique_encode, path_store= path_store)
    
    if 'vs_str_Violate' in k:
        rm.ruleGenerator_v(df_encode=df_unique_encode, path_store= path_store)
    
        


if __name__ == '__main__':
    
    import click
    
    @click.command()
    @click.option('-i', '--input_file', 'file_path', help = 'path to file')
    @click.option('-o', '--output_file', 'output_file', help = 'name of output file')
    @click.option('-g', '--group', 'group_number', help = 'this parameter is for our exp purpose')
    @click.option('-mr', '--mr', 'mr', help = 'this parameter is for our exp purpose')

    def main(file_path, output_file, group_number, mr):
        
        root_path = str(pathlib.Path().absolute()) + '/feature_extractor_outputs'
        path_rules = str(pathlib.Path().absolute()) + '/generated_rules/G' + group_number + '/' + mr
        
        try:
            os.makedirs(root_path)
        except:
            pass
        
        try:
            os.makedirs(path_rules)

        except:
            pass
        
        store_path_rules = os.path.join(path_rules, output_file + '_rules')

        if output_file.find('.csv'):
            output_file = output_file + '.csv'
            
        storage_path = os.path.join(root_path, output_file)
        data = process(tarjet_path=file_path, output_path= storage_path)
        start_rule_mining(data=data, path_store=store_path_rules)

main()