# Reading, initial position front = r
# Writing, initial position end = a
# Writing, truncate = w
# Reading and Writing, initial position front = r+
# Reading and Writing, initial position end = a+
# Reading and Writing, truncate = w+
# Create a blank file = x

# Read-only mode. The file is opened for reading, and the file pointer is placed at the beginning of the file.
def open_file_r(file):
    with open(file, 'r') as content:
        lines = content.read()
    return lines

# Opens a file for appending. The file pointer is at the end of the file if the file exists. If the file does not exist, it creates a new file for writing.
def open_file_a(file, write):
    with open(file, 'a') as content:
        content.write(write)

# Write-only mode. If the file exists, it is truncated to zero length. If the file does not exist, it is created. The file pointer is placed at the beginning of the file.
def open_file_w(file, write):
    with open(file, 'w') as content:
        content.write(write)

# Read and write mode. The file is opened for both reading and writing, and the file pointer is placed at the beginning of the file.
def open_file_rplus(file, write):
    with open(file, 'r+') as content:
        lines = content.read()
        content.write(write)
    return lines

# Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
def open_file_aplus(file, write):
    with open(file, 'a+') as content:
        lines = content.read()
        content.write(write)
    return lines

# Read and write mode. If the file exists, it is truncated to zero length. If the file does not exist, it is created. The file pointer is placed at the beginning of the file.
def open_file_wplus(file, write):
    with open(file, 'w+') as content:
        lines = content.read()
        content.write(write)
    return lines

# Open for exclusive creation, failing if the file already exists.
def open_file_x(file, write):
    with open(file, 'x') as content:
        content.write(write)
    
# If it's a CSV file. Ignores every line that starts with the second variable you pass it.
def open_csv_r(file, ignore):
    import csv
    lines = []
    with open(file, 'r') as csv_file:
        content = csv.reader(csv_file)
        for line in content:
            if line != []:
                if not line[0].strip().startswith(ignore):
                    lines.append(line)
    return lines

# Converts the contents of a folderpath into a list, including subfolders.
def folder_to_files(folder, type=''):
    import os.path
    folder = folder.strip('"')
    folder = folder.strip("'")
    files = []
    if os.path.isdir(folder):
        for name in os.listdir(folder):
            file = os.path.join(folder, name)
            if os.path.isfile(file) and file.endswith(type):
                files.append(file)
            elif os.path.isdir(file):
                # If the target is a folder, the function calls itself to loop until it hits a dead end.
                subfolder = (folder_to_files(file, type))
                for subfile in subfolder:
                    files.append(subfile)
    else:
        files.append(folder)
    return files

# Converts a list of files to a dictionary.
def files_to_dictionary(files):
    import os.path
    file_content = {}
    for file in files:
        lines = []
        with open(file, 'r', encoding='utf-8') as reader:
            for line in reader:
                lines.append(f'{line}')
        dir_name = os.path.basename(os.path.dirname(file))
        file_name = os.path.basename(file)
        file_content.update({file : [lines, dir_name, file_name]})
    return file_content

# The previous two in one.
def folder_to_dictionary(folder, type=''):
    files = folder_to_files(folder, type)
    file_content = files_to_dictionary(files)
    return file_content

# Exports a list of files to a folder.
def files_to_folder(files, output):
    import shutil
    for file in files:
        shutil.copy2(file, output)

# Get the directory, name, and extension of a file.
def get_file_parts(file):
    import os.path
    dir = os.path.dirname(file)
    name,ext = os.path.splitext(os.path.basename(file))
    return dir,name,ext

# Uses a relative path.
def match_relative_path(relative_path):
    import os
    current_dir = os.getcwd()
    path = os.path.join(current_dir, relative_path)
    return path

# Moves all files from Output to a "safe" folder.
def pardon(output_path='Output', safe_path='Pardon'):
    import os
    import shutil
    if output_path.lower() == 'output': # Default output folder.
        output_path = match_relative_path(output_path)
    file_count = len(folder_to_files(output_path)) # Check if there are already files in output.
    if file_count > 0: 
        if safe_path.lower() == 'pardon':
            safe_path = match_relative_path(safe_path)
        while os.path.exists(safe_path): # This repeats until it finds an empty safe folder.
            safe_path = match_relative_path(f'{safe_path}#')
        os.mkdir(safe_path)
        shutil.move(output_path, safe_path) # This moves the files.
        os.mkdir(output_path)
        if file_count != 1:
            print(f'Moved {file_count} files already in output to {safe_path}.')
        else:
            print(f'Moved a file already in output to {safe_path}.')

# This changes file extensions. 'target' is if you only want to change specific files, otherwise set to 'all'.
def extension_changer(new_ext, input_path='Input', output_path='Output', target='all'):
    import os
    import shutil
    # Default paths:
    if input_path.lower() == 'input':
        input_path = match_relative_path(input_path)
    if output_path.lower() == 'output':
        output_path = match_relative_path(output_path)
    pardon(output_path) # Clears output folder.
    file_list = set(folder_to_files(input_path)) # Gets the list of files.
    for file in file_list:
        old_name, ext = os.path.splitext(os.path.basename(file))
        if (ext.lower() == target.lower()) or (target.lower() == 'all'):
            new_file = os.path.join(output_path, f'{old_name}{new_ext}') # Prepares the new file.
            shutil.copy2(file, output_path) # Copy,
            os.rename(os.path.join(output_path, os.path.basename(file)), new_file) # and rename.

# This is for renaming files. 'position' is either 'start' or 'end' for where the new name goes in relation to the old name.
def namer(name, input_path='Input', output_path='Output', position='end'):
    import os
    import shutil
    # Default paths:
    if input_path.lower() == 'input':
        input_path = match_relative_path(input_path)
    if output_path.lower() == 'output':
        output_path = match_relative_path(output_path)
    pardon(output_path) # Clears output folder.
    file_list = set(folder_to_files(input_path)) # Gets the list of files.
    for file in file_list:
        old_name, ext = os.path.splitext(os.path.basename(file)) # Splits name from extension.
        if position == 'start':
            new_name = name + old_name # Adds name to the beginning of the filename.
        elif position == 'end':
            new_name = old_name + name # Adds name to the end of the filename.
        new_file = os.path.join(output_path, f'{new_name}{ext}') # Prepares the new file.
        shutil.copy2(file, output_path) # Copy,
        os.rename(os.path.join(output_path, os.path.basename(file)), new_file) # and rename.