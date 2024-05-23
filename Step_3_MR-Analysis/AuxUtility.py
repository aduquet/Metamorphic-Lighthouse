import shutil
import copy
import json
import os

class Utility(object):
    
    @staticmethod
    def getName(path):
        return path.split('/')[-1]
    
    @staticmethod
    def is_json_file(fileNme):
        return fileNme.lower().endswith('.json')
    
    @staticmethod
    def copy_file_to_directories(source, destination):
        shutil.copy2(source, destination)
        
    @staticmethod
    def copy_direct_to_directories(source_directory, destination_directory):
        # Remove the destination directory if it exists
        if os.path.exists(destination_directory):
            shutil.rmtree(destination_directory)
        # Copy the entire directory tree from source to destination
        shutil.copytree(source_directory, destination_directory)
    
    @staticmethod
    def replace_string_in_file(file_path, search_string, replace_string):
        # Check if the file exists
        if not os.path.isfile(file_path):
            return "File does not exist."
    
    @staticmethod
    def create_directories(folder_name, base_directory):
        # Function to create directories based on file names    
        # folder_name = os.path.join(base_directory, file_name)
        # Create the full path for the new folder
        new_folder_path = os.path.join(base_directory, folder_name)
        
        os.makedirs(new_folder_path, exist_ok=True)
        return new_folder_path
    
    @staticmethod
    def split_mrs(list_key_to_remove, data):
        
        for key_remove in list_key_to_remove:
                for nested_key in data:
                    if key_remove in data[nested_key]:
                        del data[nested_key][key_remove]     
        return data
    
    @staticmethod
    def change_key_name(mr_name, data):
        
        aux_per = copy.deepcopy(data)
        
        old_name_ttd = 'ttd_mr_' + mr_name
        old_name_ttd_output = 'ttd_output_mr_' + mr_name 
        old_name_vs_str = 'vs_str_mr_' + mr_name 
        old_name_vs = 'vs_mr_' + mr_name 

        for key in aux_per:
            aux_per[key]['ttd'] = aux_per[key].pop(old_name_ttd)
            aux_per[key]['ttd_output'] = aux_per[key].pop(old_name_ttd_output)
            aux_per[key]['vs_str'] = aux_per[key].pop(old_name_vs_str)
            aux_per[key]['vs'] = aux_per[key].pop(old_name_vs)
        
        return aux_per
    
    @staticmethod
    def save_json(file_path, data):
        # Open the file in write mode
        with open(file_path, 'w') as json_file:
            # Write the JSON object to the file
            json.dump(data, json_file, indent=4)