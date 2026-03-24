import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)

def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if valid_target_file == False:
        return(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    else:
        if os.path.isdir(target_file):
            return(f'Error: Cannot read to "{file_path}" as it is a directory')

        dirname = os.path.dirname(target_file)
        os.makedirs(dirname, exist_ok=True)
        
        try:
            openedfile = open(target_file, mode='w',)
            openedfile.write(content)
        except:
            return("Error: YOU LOST YOU HAHAHAHAHHA stupid")
        else:
            return(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')

