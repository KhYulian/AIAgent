import os

def is_path_within_work_dir(working_directory, path):
    work_dir_full_path = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, path))
    
    return full_path.startswith(work_dir_full_path)