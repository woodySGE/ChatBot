import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
               ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of arguments to pass to the Python script",
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if valid_target_file == False:
            return(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        else:
            if not os.path.isfile(target_file):
                return(f'Error: "{file_path}" does not exist or is not a regular file')

            if not target_file.endswith(".py"):
                return(f'Error: "{file_path}" is not a Python file')

            absolute_file_path = os.path.abspath(target_file)
            command = ["python", absolute_file_path]

            if args is not None:
                command.extend(args)

            result = subprocess.run(command,cwd=working_dir_abs,text=True,capture_output=True,timeout=30)

            returnstring = ""
        
            if not result.returncode == 0:
                returnstring = f"{returnstring}Process exited with code {result.returncode}."
                
            if not result.stderr and not result.stdout:
                returnstring = f"{returnstring} No output produced"
            else:
                returnstring = f"{returnstring} STDOUT:{result.stdout}.\n STDERR:{result.stderr}"

            return returnstring 
            
    except Exception as e:
            return f"Error: executing Python file: {e}"
            


        
        
    