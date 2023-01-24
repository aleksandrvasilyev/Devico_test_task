import json

animals_legs = {'pigs': 4, 'chickens': 2, 'cows': 4}  # How many legs have each animal


def total_number_of_legs(file):
    """
    :param file: File in json format, with number of animals the farmer has.
    :return: int value, the total amount of animals legs the farmer has.
    """
    with open(file, 'r') as f:
        total_animals = json.load(f)

    total_legs = 0

    for animal in total_animals:
        if animal in animals_legs:
            total_legs += total_animals[animal] * animals_legs[animal]
        else:
            print(f'Animal "{animal}" is not found.')

    return total_legs


print(total_number_of_legs('animals.json'))
