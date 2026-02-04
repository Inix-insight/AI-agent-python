from os import path
import os
import subprocess

def run_python_file(working_directory, file_path, args = None):
    try:
        working_absolute_path = path.abspath(working_directory)
        full_path = path.normpath(path.join(working_absolute_path, file_path))
        
        if path.commonpath([full_path, working_absolute_path]) != working_absolute_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory\n'
        
        if not path.isfile(full_path):
            return f'Error: "{file_path}" does not exist or is not a regular file\n'

        if full_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", full_path]
        if args is not None:
            command.extend(args)
        
        completed = subprocess.run(command, capture_output = True, text = True, timeout = 30)

        if completed.returncode != 0:
            output = "Process exited with code X"
        elif completed.stdout is None and completed.stderr is None:
            output = "No output produced"
        else:
            output = f"STDOUT: {completed.stdout}\nSTDERR: {completed.stderr}"
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"

