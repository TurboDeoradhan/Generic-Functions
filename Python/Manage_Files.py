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