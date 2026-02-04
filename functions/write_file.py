from os import path
import os

def write_file(working_directory, file_path, content):
    try:
        working_absolute_path = path.abspath(working_directory)
        full_path = path.normpath(path.join(working_absolute_path, file_path))
        
        if path.commonpath([full_path, working_absolute_path]) != working_absolute_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory\n'
        
        if path.isdir(full_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory\n'
        
        os.makedirs(path.dirname(full_path), exist_ok = True)
        file = open(full_path, "w")
        file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: {str(e)}"