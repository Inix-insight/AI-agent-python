from os import path
import os

def get_files_info(working_directory, directory = "."):
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