# Basic source folder input.
def get_source():
    source = input('Source folder location: ')
    return source

# Basic output folder input.
def get_output():
    output = input('Output folder location: ')
    return output

# Basic menu input.
def basic_menu(intro, options):
    print(intro)
    number = 0
    for option in options:
        number += 1
        print(f'{number}. {option.title()}')
    try:
        choice = int(input('Choose an option number: ')) - 1
        return options[choice]
    except Exception as e:
        print(f'{e}\nPlease enter a number within range.')
        basic_menu(intro, options)