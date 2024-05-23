from pathlib import Path
import pandas as pd
import traceback
import pathlib
import json
import sys
import os

all_methods_path = Path(__file__).parent / 'PATH_TO_METHODS'

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../executers'))
from adapters.adapter_inputs import AdapterInputs
from adapters.adapter_mr_checker import AdapterMRchecker

# Making sure the directory exists
if not all_methods_path.is_dir():
    raise ImportError(f"The directory {all_methods_path} does not exist")

# Add the parent directory of AllMethods to the Python path
sys.path.append(str(all_methods_path.parent))

from ROUTE_TO_METHOD import METHOD_NAME

def _get_ttd(input):
    
    return AdapterInputs(test_data_one_input = input).ttd_all_mrs(const=2)

def _get_outputs(all_inputs):
    error_message = None
    
    inputs_outputs = all_inputs.copy()
    try:
        inputs_outputs['td_output'] = METHOD_NAME(all_inputs['td'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['td_output'] = 'error'
    try:
        inputs_outputs['ttd_output_mr_per'] = METHOD_NAME(all_inputs['ttd_mr_per'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_per'] = 'error'
        
    try:
        inputs_outputs['ttd_output_mr_add'] = METHOD_NAME(all_inputs['ttd_mr_add'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_add'] = 'error'
    
    try:
        inputs_outputs['ttd_output_mr_mul'] = METHOD_NAME(all_inputs['ttd_mr_mul'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_mul'] = 'error'
    
    try:
        inputs_outputs['ttd_output_mr_inv'] = METHOD_NAME(all_inputs['ttd_mr_inv'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_inv'] = 'error'
    
    try:
        inputs_outputs['ttd_output_mr_inc'] = METHOD_NAME(all_inputs['ttd_mr_inc'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_inc'] = 'error'
    
    try:
        inputs_outputs['ttd_output_mr_exc'] = METHOD_NAME(all_inputs['ttd_mr_exc'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_exc'] = 'error'   
        
    return inputs_outputs

def mr_checker(inputs_outputs):
    
    return AdapterMRchecker(inputs_outputs,2).all_mrs_checker()

def save_json(df, output, savePath):
    df.to_json(savePath + '/' + output + '.json', indent= 4, orient="index")
    print('*** Done ***')
    print('Saved in: ', savePath + '/' + output + '.json')

def save_csv(df, output, savePath):
    df.to_csv(savePath + '/' + output + '.csv')
    print('Saved in: ', savePath + '/' + output + '.csv')
    print('*****')

if __name__ == '__main__':
    
    import click
    
    global mainDF
    mainDF = pd.DataFrame()
    
    global auxList
    auxList = []
    
    @click.command()
    @click.option('-i', '--input_path', 'input_path')
    @click.option('-o', '--output_file', 'output_file')

    def main(input_path, output_file):
        
        mainPathMRChecker = str(pathlib.Path().absolute()) + '/' + 'Logs'

        try:
            os.mkdir(mainPathMRChecker)
        except:
            pass
        
        with open(input_path, 'r') as readfiles:
            inputs = json.load(readfiles)
            json.dumps(inputs, indent=4)
            
        for i in range(0, len(inputs)):
            test_data = inputs[str(i)]['td']            
            td_ttd = _get_ttd(test_data)
            input_outputs = _get_outputs(td_ttd)
            checkers = mr_checker(input_outputs)
            
            auxList.append(checkers)

        final_df = pd.DataFrame(auxList)
        
        save_csv(final_df, output_file, mainPathMRChecker)
        save_json(final_df, output_file, mainPathMRChecker)
        
main()
    