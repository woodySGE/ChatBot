import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
               ),
        },
    ),
)

def get_files_info(working_directory, directory="."):


    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if valid_target_dir == False:
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    else:
        if directory == type(str):
            return(f'Error: "{directory}" is not a directory')

        targetstring = ""

        getalldir = os.listdir(target_dir)

        for i in getalldir:

            i = f"{target_dir}/{i}"

            getpath = os.path.abspath(i)
            getisdir = os.path.isdir(getpath)
            getisfile = os.path.isfile(i)
            getbasename = os.path.basename(getpath)

            if getisfile == True:
                getsize = os.path.getsize(getpath)
            else:
                getsize = 44
            try: 
                if targetstring == "":
                    #targetstring = "\n".join(f"- {getbasename}: file_size={getsize} bytes, is_dir={getisdir}")
                    targetstring = f"- {getbasename}: file_size={getsize} bytes, is_dir={getisdir}"
                else:
                    targetstring = f"{targetstring}\n- {getbasename}: file_size={getsize} bytes, is_dir={getisdir}"
            except:
                raise Exception("Error: Failed L bozo")
            
        return targetstring

            