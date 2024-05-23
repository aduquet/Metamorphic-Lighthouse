from pathlib import Path
import pandas as pd
import traceback
import pathlib
import json
import sys
import os

all_methods_path = Path(__file__).parent / '/Users/alduck/Documents/GitHub/SelectingConstrainingMRsScSoft/AllMethods'

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../executers'))
from adapters.adapter_inputs import AdapterInputs
from adapters.adapter_mr_checker import AdapterMRchecker

# Making sure the directory exists
if not all_methods_path.is_dir():
    raise ImportError(f"The directory {all_methods_path} does not exist")

# Add the parent directory of AllMethods to the Python path
sys.path.append(str(all_methods_path.parent))

from AllMethods.Group_03.add.src.add import add

def _get_ttd(input):
    
    return AdapterInputs(test_data_one_input = input).ttd_all_mrs(const=2)

def _get_outputs(all_inputs):
    error_message = None
    
    inputs_outputs = all_inputs.copy()
    
    try:
        inputs_outputs['td_output'] = add(all_inputs['td_a'], all_inputs['td_b'] )
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['td_output'] = 'error'
    try:
        inputs_outputs['ttd_output_mr_per'] = add(all_inputs['td_ttd_a_MR_PER'], all_inputs['td_ttd_b_MR_PER'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_per'] = 'error'
        
    try:
        inputs_outputs['ttd_output_mr_add'] = add(all_inputs['td_ttd_a_MR_ADD'], all_inputs['td_ttd_b_MR_ADD'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_add'] = 'error'
    
    try:
        inputs_outputs['ttd_output_mr_mul'] = add(all_inputs['td_ttd_a_MR_MUL'], all_inputs['td_ttd_b_MR_MUL'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_mul'] = 'error'
    
    try:
        inputs_outputs['ttd_output_mr_inv'] = add(all_inputs['td_ttd_a_MR_INV'], all_inputs['td_ttd_b_MR_INV'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_inv'] = 'error'
    
    try:
        inputs_outputs['ttd_output_mr_inc'] = add(all_inputs['td_ttd_a_MR_INC'], all_inputs['td_ttd_b_MR_INC'])
    except (TypeError, ValueError, ZeroDivisionError):
        error_message = traceback.format_exc()
        inputs_outputs['ttd_output_mr_inc'] = 'error'
    
    try:
        inputs_outputs['ttd_output_mr_exc'] = add(all_inputs['td_ttd_a_MR_EXC'], all_inputs['td_ttd_b_MR_EXC'])
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

            all_inputs = {
                'td_a' : inputs[str(i)]['td_a'],
                'td_b' :inputs[str(i)]['td_b'],
                'td_ttd_a_MR_ADD' :inputs[str(i)]['td_ttd_a_MR_ADD'],
                'td_ttd_b_MR_ADD' : inputs[str(i)]['td_ttd_b_MR_ADD'],
                'td_ttd_a_MR_EXC' :inputs[str(i)]['td_ttd_a_MR_EXC'],
                'td_ttd_b_MR_EXC' : inputs[str(i)]['td_ttd_b_MR_EXC'],
                'td_ttd_a_MR_INC' :inputs[str(i)]['td_ttd_a_MR_INC'],
                'td_ttd_b_MR_INC' : inputs[str(i)]['td_ttd_b_MR_INC'],
                'td_ttd_a_MR_INV' :inputs[str(i)]['td_ttd_a_MR_INV'],
                'td_ttd_b_MR_INV' : inputs[str(i)]['td_ttd_b_MR_INV'],
                'td_ttd_a_MR_MUL' :inputs[str(i)]['td_ttd_a_MR_MUL'],
                'td_ttd_b_MR_MUL' : inputs[str(i)]['td_ttd_b_MR_MUL'],
                'td_ttd_a_MR_PER' :inputs[str(i)]['td_ttd_a_MR_PER'],
                'td_ttd_b_MR_PER' : inputs[str(i)]['td_ttd_b_MR_PER']
            }            

            input_outputs = _get_outputs(all_inputs)
            # ttd_outputs = _get_outputs(ttd_a, ttd_b)
            checkers = mr_checker(input_outputs)
            
            auxList.append(checkers)

        final_df = pd.DataFrame(auxList)
        
        save_csv(final_df, output_file, mainPathMRChecker)
        save_json(final_df, output_file, mainPathMRChecker)
        
main()