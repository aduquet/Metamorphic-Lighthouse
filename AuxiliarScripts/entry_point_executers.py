import pandas as pd
import subprocess
import glob as gl
import pathlib
import shutil
import json
import os

def create_folder_executers(group_number):
    
    currentPath = str(pathlib.Path().absolute())
    parent_directory = os.path.dirname(currentPath)
    
    executers_folder_path = os.path.join(parent_directory, 'Step_2_MT-Process')
    
    # Check if the path exists
    if os.path.exists(executers_folder_path):
        try:
            os.mkdir(os.path.join(executers_folder_path, 'executers_' + group_number))
        except :
            pass
    else:
        os.mkdir(executers_folder_path)
    
    return os.path.join(executers_folder_path, 'executers_' + group_number)

# def create_py_file(file_name, path_file):

def replace_string_in_file(file_path, search_string, replace_string):
    # Check if the file exists
    if not os.path.isfile(file_path):
        return "File does not exist."

    # Read and replace content
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        content = content.replace(search_string, replace_string)

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(content)
        print (f"Replaced '{search_string}' with '{replace_string}' in {file_path}.")
    except Exception as e:
        print( str(e))
        pass
    
    
            
# Function to copy the source file into each target directory
def copy_file_to_directories(source, destination):
    shutil.copy2(source, destination)
    print(f"Copied to: {destination}")

if __name__ == '__main__':
    import click
    
    @click.command()
    @click.option('-i', '--file_info_path', 'info_path', help = '')
    
    def main(info_path):
        ''' ['groupID', 'fullPathToFunctionDir', 'fullPathToFunctionSrcDir',
        'fullPathToFunctionTestDir', 'fullPathToFunctionPYfile',
        'functionName']'''
        
        template_path = '/Users/alduck/Documents/Github/SelectingConstrainingMRsScSoft/Step_2_MT-Process/template_executer.py'
        
        data_info = pd.read_csv(info_path, index_col=0)
        
        parent_directory = os.path.dirname(str(pathlib.Path().absolute()))
        
        list_groups = list(set(data_info['groupID']))
        
        for i in list_groups:
            group_number = i.split('_')[-1]
            folder_path = create_folder_executers('G' + group_number)
            print(folder_path)
            subset_aux = data_info[data_info['groupID'] == i]
            # print(subset_aux)
            if i != 'Group_01':
                for index,row in subset_aux.iterrows():
                    file_name = row['functionName'] + '_executer.py'
                    new_file_path = os.path.join(folder_path, file_name)
                    route_to_method = 'AllMethods.' + i + '.' + row['functionName'] + '.src.' + row['functionName']
                    with open(new_file_path, "w") as f:
                        pass
                    
                    # Copy the content of the template file to the new file
                    try:
                        with open(template_path, 'r') as template_file:
                            template_content = template_file.read()
                        with open(new_file_path, 'w') as new_file:
                            new_file.write(template_content)
                    except IOError as e:
                        print(f"Error: {e}")

                    replace_string_in_file(file_path=new_file_path , search_string= "'PATH_TO_METHODS'", replace_string= "'/Users/alduck/Documents/GitHub/SelectingConstrainingMRsScSoft/AllMethods'")
                    replace_string_in_file(file_path=new_file_path , search_string= "METHOD_NAME", replace_string= row['functionName'])
                    replace_string_in_file(file_path=new_file_path , search_string= "ROUTE_TO_METHOD", replace_string= route_to_method)

                    # print(file_name)
                    
                
        # print("Parent directory:", parent_directory)
        
        # print(data_info.keys())
        # print(str(pathlib.Path().absolute()))
        
main()