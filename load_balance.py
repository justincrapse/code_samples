import sys
import random


# select weighted random server based on server capacity:
def select_server(server_dict):
    # Python dicts are "insertion ordered" by default in Python 3.6.
    return random.choices(population=list(server_dict.keys()), weights=list(server_dict.values()), k=1)[0]


def select_server_older_python(server_dict):
    """ for python 3.5 and lower """
    ordered_population = []
    ordered_weights = []
    for key, value in server_dict.items():
        ordered_population.append(key)
        ordered_weights.append(value)
    return random.choices(population=list(server_dict.keys()), weights=list(server_dict.values()), k=1)[0]


if __name__ == '__main__':
    function_to_test = select_server
    assert len(sys.argv) > 1, 'Must provide server names and sizes seperated by a colon. E.g.: "X:5 Y:7"'
    args_dict = {x.split(':')[0]: int(x.split(':')[1]) for x in sys.argv[1:]}
    print(function_to_test(server_dict=args_dict))

