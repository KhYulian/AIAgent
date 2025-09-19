import os
import subprocess

from utils.is_path_within_work_dir import is_path_within_work_dir
from functions.get_file_content import get_file_content

def run_python_file(working_directory, file_path, args=[]):    
    if not is_path_within_work_dir(working_directory, file_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        cmd = ["python", full_path]
        if args:
            cmd.extend(args)
        result =  subprocess.run(cmd, timeout=30, cwd=working_directory, text=True, capture_output=True)
        if not result.stdout and not result.stderr:
            return "No output produced."
        
        return "{out}{err}{err_code}".format(out="STDOUT: " + result.stdout if result.stdout else "", err="\nSTDERR: " + result.stderr if result.stderr else "", err_code="\nProcess exited with code " + result.returncode if result.returncode != 0 else "")

    except Exception as e:
        return f"Error: executing Python file: {e}"