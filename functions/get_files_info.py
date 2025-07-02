import os

def get_files_info(working_directory, directory=None):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        if directory is None:
            directory = abs_working_directory
        if not os.path.isabs(directory):
            directory = os.path.join(abs_working_directory, directory)
        abs_directory = os.path.abspath(directory)
        if not (abs_directory.startswith(abs_working_directory + os.sep) or abs_directory == abs_working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(directory):
            return f'Error: "{directory}" is not a directory'
        file_contents = os.listdir(abs_directory)
        item_details_list = []
        for item in file_contents:
            full_item_path = os.path.join(abs_directory, item)
            is_dir = False
            if os.path.isdir(full_item_path):
                is_dir = True
            size = os.path.getsize(full_item_path)
            item_details = f"- {item}: file_size={size} bytes, is_dir={is_dir}"
            item_details_list.append(item_details)        
        item_details_string = "\n".join(item_details_list)
        return item_details_string
    except OSError as e:
            return "Error: " + str(e)