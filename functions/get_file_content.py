from os import path
import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        working_absolute_path = path.abspath(working_directory)
        full_path = path.normpath(path.join(working_absolute_path, file_path))
        
        if path.commonpath([full_path, working_absolute_path]) != working_absolute_path:
            return f"Error: Cannot list \"{file_path}\" as it is outside the permitted working directory\n"
        
        if not path.isfile(full_path):
            return f"Error: File not found or is not a regular file: \"{file_path}\"\n"
        
        file = open(full_path)
        content = file.read(MAX_CHARS)
        if file.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    
    except Exception as e:
        return f"Error: {str(e)}"

schema_get_file_content = types.FunctionDeclaration(
    name = "get_file_content",
    description = "Read the file in a specified directory relative to the working directory and return the first 10000 characters truncated",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "file_path": types.Schema(
                type = types.Type.STRING,
                description = "Directory path to file to read from, relative to the working directory (default is the working directory itself)",
            ),
        },
        required = ["file_path"],
    ),
)