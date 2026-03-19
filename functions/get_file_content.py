#from constants import MAX_CHARS
import os
def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    if valid_target_file == False:
        return(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')

    if not os.path.isfile(target_file):
        return(f'Error: File not found or is not a regular file: "{file_path}"')

    try:
        veryfile = os.path.abspath(target_file)
        funny = open(veryfile)
        funnyv2 = funny.read(10000)
        return funnyv2
    except:
        return "Error: bro got rolled"

    

