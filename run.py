import csv
from collections import namedtuple

Seps = namedtuple('seps', ['sep', 'decimal', 'thousands'])



def guess_csv(argument=None):
    result_dict = {
        ';': 0,
        ',': 0,
        '.': 0
    }

    for line in csv.reader(open(argument, "r")):
        result_dict[';'] += line[0].count(';')
        result_dict[','] += line[0].count(',')
        result_dict['.'] += line[0].count('.')
    # print(result_dict)

    for key, value in result_dict.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if value == max(result_dict.values()):
            seps = key
        elif value == min(result_dict.values()):
            thousands = key
        else:
            decimal = key

    result = Seps(seps, thousands, decimal)
    # result = namedtuple('seps', (seps, decimal, thousands))
    return result



print('start')
print(guess_csv("input_1.csv"))
print(guess_csv("input_2.csv"))
print(guess_csv("input_3.csv"))