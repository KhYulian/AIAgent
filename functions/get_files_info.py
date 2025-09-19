import os

from utils.is_path_within_work_dir import is_path_within_work_dir

def get_files_info(working_directory, directory="."):
    if not is_path_within_work_dir(working_directory, directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    full_path = os.path.abspath(os.path.join(working_directory, directory))

    is_dir = os.path.isdir(full_path)
    if not is_dir:
        return f'Error: "{directory}" is not a directory'
    
    try:
        dir_content = os.scandir(full_path)
        content_str = ""
        for dir_entry in dir_content:
            entry_str = f"{dir_entry.name}: file_size={dir_entry.stat().st_size}, is_dir={dir_entry.is_dir()}"
            content_str += entry_str + "\n"

        return content_str
    except Exception as e:
        return f"Error listing files: {e}"
    