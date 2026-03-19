import os

def run_python_file(working_directory, file_path, args=None):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if valid_target_file == False:
        return(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    else:
        if os.path.isfile(target_file):
            return(f'Error: "{file_path}" does not exist or is not a regular file')

        if not target_file.endswith(".py"):
            return(f'Error: "{file_path}" is not a Python file')

        absolute_file_path = os.path.abspath(target_file)
        command = ["python", absolute_file_path]

        command = command.extend(args)

        
        
    