# Creates a simple dictionary from content.
def dictionary_create(content):
    dictionary = {}
    # The first value becomes the key.
    for line in content:
        list = []
        # From the second slot to the end becomes the dictionary content.
        for item in line[1:]:
            list.append(item.strip())
        dictionary.update({line[0].strip() : list})
    return dictionary

# Simple reader for a dicitonary.
def dictionary_read(dictionary):
    for i in dictionary:
        print(i)
        print(dictionary[i])

# Converts a file dictionary to file in the specified path.
def dictionary_to_files(content, path):
    import os.path
    # Checks for a valid path, or creates it.
    try:
        if os.path.isdir(path):
            out = path
        else:
            out = os.path.dirname(path)
        if not os.path.exists(out):
            os.mkdir(out)
    except Exception as e:
        print(f'{e} occurred as a result of: {path}')

    # Key = file name, 0 = content, 1 = folder, 2 = file name.
    for file in content:
        folder = os.path.join(out, content[file][1])
        if not os.path.exists(folder):
            os.mkdir(folder)
        path = os.path.join(folder, content[file][2])
        # Replaces files to avoid problems.
        with open(path, 'w', encoding='utf-8') as inscription:
            for line in content[file][0]:
                try:
                    inscription.write(line)
                except Exception as e:
                    print(f'{e} occurred as a result of: {file} {line}')
def flip_dictionary(dictionary):
    flipped = {}
    for key in dictionary:
        for item in dictionary[key]:
            flipped.update({item : key})
    return flipped
# Finds duplicates in a list. Position can be set to 'full' to search each line, or a number for a specific index of each line.
def find_duplicates(list, position='full'):
    items = []
    duplicates = []
    if position == 'full':
        for item in list:
            if item not in items:
                items.append(item)
            elif item not in duplicates:
                duplicates.append(item)
                print(item)
    else:
        position = int(position)
        for item in list:
            if item[position] not in items:
                items.append(item[position])
            elif item[position] not in duplicates:
                duplicates.append(item[position])
                print(item[position])