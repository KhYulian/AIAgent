import os

from config import MAX_FILE_SIZE
from utils.is_path_within_work_dir import is_path_within_work_dir

def get_file_content(working_directory, file_path):
    if not is_path_within_work_dir(working_directory, file_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    try: 
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        is_file = os.path.isfile(full_path)
        
        if not is_file:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(full_path, "r") as f:
            content = f.read(MAX_FILE_SIZE)
            if os.path.getsize(full_path) > MAX_FILE_SIZE:
                content += (
                    f'[...File "{file_path}" truncated at {MAX_FILE_SIZE} characters]'
                )
        return content
    except Exception as e:
        return f"Error: {e}"
        