import csv
from collections import namedtuple

from arguments import argument_1, argument_2, argument_3, argument_4, argument_5

Seps = namedtuple('seps', ['sep', 'decimal', 'thousands'])


def guess_csv(argument=None):
    result_dict = {
        ';': 0,
        ',': 0,
        '.': 0,
        '|': 0
    }
    lines = argument.split('\n')
    for key in result_dict.keys():
        if lines[0].count(key):
            seps = key

    for line in lines[1:]:
        if line:
            rows = line.split(seps)
            for row in rows:
                result_dict[','] += row.count(',')
                result_dict['.'] += row.count('.')
    # print(result_dict)
    decimal = None
    thousands = None
    for key, value in result_dict.items():
        if key in [',', '.']:
            if value == max(result_dict.values()):
                decimal = key
            elif value == min(result_dict.values()):
                pass
            else:
                thousands = key

    result = Seps(seps, decimal, thousands)
    return result




print('start')
print(guess_csv(argument_1))
print(guess_csv(argument_2))
print(guess_csv(argument_3))
print(guess_csv(argument_4))
print(guess_csv(argument_5))
print('stop')
