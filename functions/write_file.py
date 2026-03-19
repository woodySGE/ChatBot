import os

def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if valid_target_file == False:
        print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    
    if not os.path.isdir(target_file):
        print(f'Error: Cannot write to "{file_path}" as it is a directory')

    os.mkdir(target_file, exist_ok=True)
    
    try:
        openedfile = open(file_path, mode='w',)
        openedfile.write(content)
    except:
        return "Error: YOU LOST YOU HAHAHAHAHHA stupid"
    else:
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
