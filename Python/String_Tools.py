# Checks for numbers.
def has_numbers(input):
    import re
    return bool(re.search(r'\d', input))

# Returns a properly titled string. May need adjustments.
def title_case(untitled):
    import re
    detitled = untitled.capitalize()
    titled = re.sub(r'( |(?<=\())([a-z])', lambda x: x.group().upper(), detitled)
    titled = re.sub(r'( |(?<=\-))([a-z])', lambda x: x.group().upper(), detitled)
    if bool(re.search(r'\d', titled)):
        titled = titled.replace(' Am', ' AM')
        titled = titled.replace(' am', ' AM')
        titled = titled.replace(' Pm', ' PM')
        titled = titled.replace(' pm', ' PM')
    titled = titled.replace(' The ', ' the ')
    titled = titled.replace(' A ', ' a ')
    titled = titled.replace(' An ', ' an ')
    titled = titled.replace(' And ', ' and ')
    titled = titled.replace(' But ', ' but ')
    titled = titled.replace(' Or ', ' or ')
    titled = titled.replace(' Yet ', ' yet ')
    titled = titled.replace(' Of ', ' of ')
    titled = titled.replace(' In ', ' in ')
    titled = titled.replace(' To ', ' to ')
    titled = titled.replace(' As ', ' as ')
    titled = titled.replace(' At ', ' at ')
    titled = titled.replace(' By ', ' by ')
    titled = titled.replace(' For ', ' for ')
    titled = titled.replace(' From ', ' from ')
    titled = titled.replace(' In ', ' in ')
    titled = titled.replace(' Is ', ' is ')
    titled = titled.replace(' Into ', ' into ')
    titled = titled.replace(' Nor ', ' nor ')
    titled = titled.replace(' On ', ' on ')
    titled = titled.replace(' So ', ' so ')
    titled = titled.replace(' Than ', ' than ')
    titled = titled.replace(' That ', ' that ')
    titled = titled.replace(' With ', ' with ')
    titled = titled.replace('K.k.', 'K.K.')
    return titled