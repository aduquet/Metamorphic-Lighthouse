import os
import json
import pathlib
import glob as gl
import pandas as pd
from frequency import GetViolationsNoViolations

def getname(fullpath):
      return fullpath.split('/')[-1]

def is_json_file(filename):
    return filename.lower().endswith('.json')

def process(tarjet_paths, output_path):
      
      mainDF = {}
      auxMain = []
      mainDF_cnt = {}
      auxMain_cnt = []
      
      for i in tarjet_paths:
            
            if (is_json_file(getname(i))):
                  with open(i, 'r') as file:
                    data = json.load(file)
              
                  vs_status_per = GetViolationsNoViolations(data, 'vs_str_mr_per')
                  vs_status_add = GetViolationsNoViolations(data, 'vs_str_mr_add')
                  vs_status_mul = GetViolationsNoViolations(data, 'vs_str_mr_mul')
                  vs_status_inv = GetViolationsNoViolations(data, 'vs_str_mr_inv')
                  vs_status_inc = GetViolationsNoViolations(data, 'vs_str_mr_inc')
                  vs_status_exc = GetViolationsNoViolations(data, 'vs_str_mr_exc')
                  
                  mainDF = {
                    'method_name': getname(i),
                    
                    'MR_per_v':     vs_status_per.getViolations(),
                    'MR_per_nv':    vs_status_per.getNoViolations(),
                    'MR_per_e':     vs_status_per.getExceptions(),
                    
                    'MR_add_v':     vs_status_add.getViolations(),
                    'MR_add_nv':    vs_status_add.getNoViolations(),
                    'MR_add_e':     vs_status_add.getExceptions(),
                    
                    'MR_mul_v':     vs_status_mul.getViolations(),
                    'MR_mul_nv':    vs_status_mul.getNoViolations(),
                    'MR_mul_e':     vs_status_mul.getExceptions(),
                    
                    'MR_inv_v':     vs_status_inv.getViolations(),
                    'MR_inv_nv':    vs_status_inv.getNoViolations(),
                    'MR_inv_e':     vs_status_inv.getExceptions(),
                    
                    'MR_inc_v':     vs_status_inc.getViolations(),
                    'MR_inc_nv':    vs_status_inc.getNoViolations(),
                    'MR_inc_e':     vs_status_inc.getExceptions(),
                    
                    'MR_exc_v':     vs_status_exc.getViolations(),
                    'MR_exc_nv':    vs_status_exc.getNoViolations(),
                    'MR_exc_e':     vs_status_exc.getExceptions(),
                  }
                  auxMain.append(mainDF)

                  mainDF_cnt = {
                    'method_name': getname(i),
                    
                    'MR_per_v_cnt': vs_status_per.getViolations_cnt(),
                    'MR_per_nv_cnt':vs_status_per.getNoViolations_cnt(),
                    'MR_per_e_cnt': vs_status_per.getError_cnt(),
                    
                    'MR_add_v_cnt': vs_status_add.getViolations_cnt(),
                    'MR_add_nv_cnt':vs_status_add.getNoViolations_cnt(),
                    'MR_add_e_cnt': vs_status_add.getError_cnt(),       
                    
                    'MR_mul_v_cnt': vs_status_mul.getViolations_cnt(),
                    'MR_mul_nv_cnt':vs_status_mul.getNoViolations_cnt(),
                    'MR_mul_e_cnt': vs_status_mul.getError_cnt(),       
                    
                    'MR_inv_v_cnt': vs_status_inv.getViolations_cnt(),
                    'MR_inv_nv_cnt':vs_status_inv.getNoViolations_cnt(),
                    'MR_inv_e_cnt': vs_status_inv.getError_cnt(),       
                    
                    'MR_inc_v_cnt': vs_status_inc.getViolations_cnt(),
                    'MR_inc_nv_cnt':vs_status_inc.getNoViolations_cnt(),
                    'MR_inc_e_cnt': vs_status_inc.getError_cnt(),       
                    
                    'MR_exc_v_cnt': vs_status_exc.getViolations_cnt(),
                    'MR_exc_nv_cnt':vs_status_exc.getNoViolations_cnt(),
                    'MR_exc_e_cnt': vs_status_exc.getError_cnt(),                             
                  }
                  auxMain_cnt.append(mainDF_cnt)
      
      finalDF = pd.DataFrame(auxMain)
      finalDF = finalDF.sort_values(by='method_name')
      
      finalDF_cnt = pd.DataFrame(auxMain_cnt)
      finalDF_cnt = finalDF_cnt.sort_values(by='method_name')
      
      finalDF.to_csv(output_path + '/avg_v_nv_e.csv')     
      finalDF_cnt.to_csv(output_path + '/cnt_v_vn_e.csv')    


if __name__ == '__main__':
  
  import click
  
  @click.command()
  @click.option('-i', '--file', 'root_file_path', help = 'Root file path')
  @click.option('-g', '--group', 'group_number', help = 'path were outputs will be saved')
  
  def main(root_file_path, group_number):
        
        root_path = str(pathlib.Path().absolute()) + '/Group_' + group_number + '/frequency_analysis'
        try:
            os.makedirs(root_path)
        except:
            pass
          
        target_paths = gl.glob(root_file_path)        
        process(tarjet_paths=target_paths, output_path= root_path)

main()