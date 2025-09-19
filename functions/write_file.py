import os
from google.genai import types

from utils.is_path_within_work_dir import is_path_within_work_dir

def write_file(working_directory, file_path, content):
    if not is_path_within_work_dir(working_directory, file_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not os.path.exists(abs_file_path):
        try:
            os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
        return f'Error: "{file_path}" is a directory, not a file'
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: writing to file: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="If file does not exist - creates a file and writes content to it. Otherwise existing file is overwritten with new content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to the file that should be written. Restricted to working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Text content that will be written to the file"
            )
        },
    ),
)