from os import path
import os
from google.genai import types

def get_files_info(working_directory, directory = "."):
    try:
        working_absolute_path = path.abspath(working_directory)
        full_path = path.normpath(path.join(working_absolute_path, directory))
        
        if path.commonpath([full_path, working_absolute_path]) != working_absolute_path:
            return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory\n"
        
        if not path.isdir(full_path):
            return f"Error: \"{directory}\" is not a directory\n"
        
        format = ""
        for item in os.listdir(full_path):
            format += f"  - {item}: file_size={path.getsize(path.join(full_path, item))} bytes, is_dir={path.isdir((path.join(full_path, item)))}\n"
        return format
    
    except Exception as e:
        return f"Error: {str(e)}"

schema_get_files_info = types.FunctionDeclaration(
    name = "get_files_info",
    description = "Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "directory": types.Schema(
                type = types.Type.STRING,
                description = "Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)