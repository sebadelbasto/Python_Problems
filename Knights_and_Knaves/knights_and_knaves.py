from collections import defaultdict
from itertools import product


def decompose_sentence(lines):
    sentence = []
    punctuations = []
    for i in range(len(lines)):
        if lines[i].endswith(','):
            lines[i] = lines[i][:-1]
        if lines[i].endswith('"'):
            if not lines[i][-2:-1].isalpha():
                lines[i] = lines[i].replace(lines[i][-2:], lines[i][:-3:-1])

        if lines[i].endswith('.') or lines[i].endswith('!') or lines[i].endswith('?'):
            punctuations.append(i)
            lines[i] = lines[i][:-1]

    if punctuations:
        sentence.append([lines[i] for i in range(punctuations[0] + 1)])
        for j in range(len(punctuations) - 1):
            sentence.append([lines[k] for k in range(punctuations[j] + 1, punctuations[j + 1] + 1)])
    return sentence


def find_saying_names(quote):
    situation = {'A': ' least ', 'B': ' most ', 'C': 'exactly one of ', 'D': 'all of ', 'E': ' and ', 'F': ' or ',
                 'G': ' is ', 'H': ' am '}
    saying_names = defaultdict(list)
    for key, value in quote.items():
        for line in range(len(value)):
            if value[line][0].istitle:
                if value[line][0] == 'Exactly' or value[line][0] == 'All':
                    quote[key][line][0] = value[line][0].lower()
            value[line] = ' ' + ' '.join(value[line][i] for i in range(len(value[line])))
            if ' I ' in value[line]:
                value[line] = value[line].replace(' I ', f' {key} ')

            if 'Knight' in value[line] or 'Knights' in value[line]:
                for i, j in situation.items():
                    if j in value[line]:
                        saying_names[key, i + '1'].append(value[line])
                        break
            elif 'Knave' in value[line] or 'Knaves' in value[line]:
                for i, j in situation.items():
                    if j in value[line]:
                        saying_names[key, i + '2'].append(value[line])
                        break

    return saying_names


def find_names(line):
    sir_name = set()
    quote = defaultdict(list)
    for i in range(len(line)):
        sentence_index = []
        sirs_index = []
        for j in range(len(line[i])):

            if line[i][j].endswith(','):
                line[i][j] = line[i][j][:-1]

            if 'Sirs' in line[i][j]:
                sirs_index.append(j)
            elif 'Sir' in line[i][j]:
                sir_name = sir_name.union([line[i][j + 1]])

            if line[i][j].startswith('"'):
                sentence_index.append(j)
                line[i][j] = line[i][j][1:]
            elif line[i][j].endswith('"'):
                sentence_index.append(j)
                line[i][j] = line[i][j][:-1]
        if sentence_index:
            without_quote = line[i][:sentence_index[0]] + line[i][sentence_index[1] + 1:]
            quote[without_quote[without_quote.index('Sir') + 1]].append([line[i][j] \
                                                                         for j in range(sentence_index[0],
                                                                                        sentence_index[1] + 1)])

        if sirs_index:
            for k in range(sirs_index[0] + 1, len(line[i])):
                if line[i][k] == 'and':
                    sir_name = sir_name.union([line[i][m] for m in range(sirs_index[0] + 1, k)])
                    sir_name = sir_name.union([line[i][k + 1]])

    sir_name = list(sir_name)
    return sorted(sir_name), quote


def reffered_names(saying_names, sir_name):
    saying_names_1 = defaultdict(list)
    for key, value in saying_names.items():
        for k in range(len(value)):
            a = [None] * len(sir_name)
            if ' us ' in value[k]:
                a = [1] * len(sir_name)
            else:
                for i in range(len(sir_name)):
                    if sir_name[i] not in value[k]:
                        continue
                    else:
                        a[i] = 1
            saying_names_1[key].append(a)

    return saying_names_1


def construct_truth_table(sir_name, names):
    truth_table = list(product((0, 1), repeat=len(sir_name)))
    truth_table = dict.fromkeys(truth_table, True)

    for truth in truth_table:
        for key, value in names.items():
            name, situation = key
            for k in range(len(value)):
                a = 0
                num = 0
                for j in range(len(value[k])):
                    if value[k][j]:
                        a += truth[j]
                        num += 1
                if situation in {'D2', 'E2', 'H2', 'G2'}:
                    if truth[sir_name.index(name)] != (a == 0):
                        if truth_table[truth]:
                            truth_table[truth] = False
                        break
                if situation in {'C1', 'H1', 'G1'}:
                    if truth[sir_name.index(name)] != (a == 1):
                        if truth_table[truth]:
                            truth_table[truth] = False
                        break
                if situation in {'A1', 'F1'}:
                    if truth[sir_name.index(name)] != (a >= 1):
                        if truth_table[truth]:
                            truth_table[truth] = False
                        break
                if situation in {'A2', 'F2'}:
                    if truth[sir_name.index(name)] != (a < num):
                        if truth_table[truth]:
                            truth_table[truth] = False
                        break
                if situation in {'D1', 'E1'}:
                    if truth[sir_name.index(name)] != (a == num):
                        if truth_table[truth]:
                            truth_table[truth] = False
                        break
                if situation in {'D1', 'E1'}:
                    if truth[sir_name.index(name)] != (a == num):
                        if truth_table[truth]:
                            truth_table[truth] = False
                        break
                if situation in {'B1'}:
                    if truth[sir_name.index(name)] != (a <= 1):
                        if truth_table[truth]:
                            truth_table[truth] = False
                        break
                if situation in {'B2'}:
                    if truth[sir_name.index(name)] != (a >= num - 1):
                        if truth_table[truth]:
                            truth_table[truth] = False
                        break
                if situation in {'C2'}:
                    if truth[sir_name.index(name)] != (a == num - 1):
                        if truth_table[truth]:
                            truth_table[truth] = False
                        break

    return truth_table


def solve_puzzle(lines):
    sir_name, quote = find_names(decompose_sentence(lines))

    try:
        saying_names = find_saying_names(quote)
        reffered_saying_name = reffered_names(saying_names, sir_name)
        truth_table = construct_truth_table(sir_name, reffered_saying_name)

        result = []
        for i in truth_table:
            if truth_table[i]:
                result.append(i)

    except Exception:
        result = []

    return sir_name, result


def display_results(sir_name, result):
    print('The Sirs are: {}'.format(' '.join(sir_name)))
    if len(result) == 0:
        print('There is no solution.')
    elif len(result) == 1:
        print('There is a unique solution:')
        for i in range(len(sir_name)):
            if result[0][i] == 1:
                print('Sir {0} is a Knight.'.format(sir_name[i]))
            else:
                print('Sir {0} is a Knave.'.format(sir_name[i]))
    elif len(result) > 1:
        print('There are {0} solutions.'.format(len(result)))


def filter_punctionations():
    with open(file) as f:
        lines = f.read()
        if lines.find('""', None):
            lines = lines.replace('""', '" "')
        if lines.find(':"', None):
            s_read = lines.replace(':"', ': "')
        lines = s_read.split()

    return lines


if __name__ == '__main__':
    file = input('Which text file do you want to use for the puzzle? ')

    lines = filter_punctionations()

    sir_name, result = solve_puzzle(lines)
    display_results(sir_name, result)
