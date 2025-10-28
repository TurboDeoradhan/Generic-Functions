# Creates a simple dictionary from content.
def dictionary_create(content):
    dictionary = {}
    # The first value becomes the key.
    for line in content:
        list = []
        # From the second slot to the end becomes the dictionary content.
        for item in line[1:]:
            list.append(item)
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