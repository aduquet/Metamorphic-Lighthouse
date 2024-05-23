from AuxUtility import Utility
import glob as gl
import pathlib
import json
import copy

def startProcess(tarjet_paths, output_path):
    
    for i in tarjet_paths:
        
        file_name = Utility.getName(i)
        folder_name = file_name.split('.')[0]
        
        new_path = Utility.create_directories(folder_name= folder_name, base_directory=output_path)
        
        if(Utility.is_json_file(fileNme=file_name)):
            
            with open(i, 'r') as file:
                data = json.load(file)
                
            per_data = copy.deepcopy(data)
            add_data = copy.deepcopy(data)
            mul_data = copy.deepcopy(data)
            inv_data = copy.deepcopy(data)
            inc_data = copy.deepcopy(data)
            exc_data = copy.deepcopy(data)
            
            per_list = ['ttd_mr_add', 'ttd_mr_mul', 'ttd_mr_inv', 'ttd_mr_inc', 'ttd_mr_exc',
                        'ttd_output_mr_add', 'ttd_output_mr_mul', 'ttd_output_mr_inv', 'ttd_output_mr_inc', 'ttd_output_mr_exc',
                        'vs_str_mr_add', 'vs_str_mr_mul', 'vs_str_mr_inv', 'vs_str_mr_inc', 'vs_str_mr_exc',
                        'vs_mr_add', 'vs_mr_mul', 'vs_mr_inv', 'vs_mr_inc', 'vs_mr_exc']

            per = Utility.split_mrs(list_key_to_remove=per_list, data= per_data)
            per = Utility.change_key_name(mr_name='per', data=per)
            Utility.save_json(new_path+'/per.json', per)
            
            add_list = ['ttd_mr_per', 'ttd_mr_mul', 'ttd_mr_inv', 'ttd_mr_inc', 'ttd_mr_exc',
                        'ttd_output_mr_per', 'ttd_output_mr_mul', 'ttd_output_mr_inv', 'ttd_output_mr_inc', 'ttd_output_mr_exc',
                        'vs_str_mr_per', 'vs_str_mr_mul', 'vs_str_mr_inv', 'vs_str_mr_inc', 'vs_str_mr_exc',
                        'vs_mr_per', 'vs_mr_mul', 'vs_mr_inv', 'vs_mr_inc', 'vs_mr_exc']
            add = Utility.split_mrs(list_key_to_remove=add_list, data= add_data)
            add = Utility.change_key_name(mr_name='add', data=add)
            Utility.save_json(new_path+'/add.json', add)
            
            mul_list = ['ttd_mr_add', 'ttd_mr_per', 'ttd_mr_inv', 'ttd_mr_inc', 'ttd_mr_exc',
                        'ttd_output_mr_add', 'ttd_output_mr_per', 'ttd_output_mr_inv', 'ttd_output_mr_inc', 'ttd_output_mr_exc',
                        'vs_str_mr_add', 'vs_str_mr_per', 'vs_str_mr_inv', 'vs_str_mr_inc', 'vs_str_mr_exc',
                        'vs_mr_add', 'vs_mr_per', 'vs_mr_inv', 'vs_mr_inc', 'vs_mr_exc']
            mul = Utility.split_mrs(list_key_to_remove=mul_list, data= mul_data)
            mul = Utility.change_key_name(mr_name='mul', data=mul)
            Utility.save_json(new_path+'/mul.json', mul)
            
            inv_list = ['ttd_mr_add', 'ttd_mr_mul', 'ttd_mr_per', 'ttd_mr_inc', 'ttd_mr_exc',
                        'ttd_output_mr_add', 'ttd_output_mr_mul', 'ttd_output_mr_per', 'ttd_output_mr_inc', 'ttd_output_mr_exc',
                        'vs_str_mr_add', 'vs_str_mr_mul', 'vs_str_mr_per', 'vs_str_mr_inc', 'vs_str_mr_exc',
                        'vs_mr_add', 'vs_mr_mul', 'vs_mr_per', 'vs_mr_inc', 'vs_mr_exc']
            inv = Utility.split_mrs(list_key_to_remove=inv_list, data= inv_data)
            inv = Utility.change_key_name(mr_name='inv', data=inv)
            Utility.save_json(new_path+'/inv.json', inv)
            
            inc_list = ['ttd_mr_add', 'ttd_mr_mul', 'ttd_mr_inv', 'ttd_mr_per', 'ttd_mr_exc',
                        'ttd_output_mr_add', 'ttd_output_mr_mul', 'ttd_output_mr_inv', 'ttd_output_mr_per', 'ttd_output_mr_exc',
                        'vs_str_mr_add', 'vs_str_mr_mul', 'vs_str_mr_inv', 'vs_str_mr_per', 'vs_str_mr_exc',
                        'vs_mr_add', 'vs_mr_mul', 'vs_mr_inv', 'vs_mr_per', 'vs_mr_exc']
            inc = Utility.split_mrs(list_key_to_remove=inc_list, data= inc_data)
            inc = Utility.change_key_name(mr_name='inc', data=inc)
            Utility.save_json(new_path+'/inc.json', inc)
            
            exclist = ['ttd_mr_add', 'ttd_mr_mul', 'ttd_mr_inv', 'ttd_mr_inc', 'ttd_mr_per',
                        'ttd_output_mr_add', 'ttd_output_mr_mul', 'ttd_output_mr_inv', 'ttd_output_mr_inc', 'ttd_output_mr_per',
                        'vs_str_mr_add', 'vs_str_mr_mul', 'vs_str_mr_inv', 'vs_str_mr_inc', 'vs_str_mr_per',
                        'vs_mr_add', 'vs_mr_mul', 'vs_mr_inv', 'vs_mr_inc', 'vs_mr_per']
            exc = Utility.split_mrs(list_key_to_remove=exclist, data= exc_data)
            exc = Utility.change_key_name(mr_name='exc', data=exc)
            Utility.save_json(new_path+'/exc.json', add)
            
if __name__ == '__main__':

    import click
    
    @click.command()
    @click.option('-i', '--file', 'root_file_path', help = 'Root file path')
    @click.option('-g', '--group', 'group_number', help = 'group number')
    
    def main(root_file_path, group_number):
        
        root_path_for_output = str(pathlib.Path().absolute()) + '/Group_' + group_number
        
        target_paths = gl.glob(root_file_path)
        startProcess(tarjet_paths=target_paths, output_path=root_path_for_output)
        
main()