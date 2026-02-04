from os import path
import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        working_absolute_path = path.abspath(working_directory)
        full_path = path.normpath(path.join(working_absolute_path, file_path))
        
        if path.commonpath([full_path, working_absolute_path]) != working_absolute_path:
            return f"Error: Cannot list \"{file_path}\" as it is outside the permitted working directory\n"
        
        if not path.isfile(full_path):
            return f"Error: File not found or is not a regular file: \"{file_path}\""
        
        file = open(full_path)
        content = file.read(MAX_CHARS)
        if file.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    
    except Exception as e:
        return f"Error: {str(e)}"