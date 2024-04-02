"""
Make a graph for the time spent per sprint.

Remember: You have to run it with the closed issues csv.
Parameters: csvFileName, team, SprintNumber

run: python3 times.py csvFileName GrupoName SprintNumber

João Moreira
"""

import matplotlib.pyplot as plt
import sys
import csv


def ReadCsv(filename, Sprint, team):
    """Read a csv file.

    filename -> name of file
    return: Dictonary with [[name, timeSpend], ...]
    """
    spent = {}
    with open(filename, 'r') as file:
        text = csv.reader(file)
        for line in text:
            if team in line[-3] and Sprint in line[-3]:
                print(line[0], " - ", line[7], " - ", int(line[-1])/3600, "H")
                if line[7] in spent:
                    spent[line[7]] += int(line[-1]) / 3600
                else:
                    spent[line[7]] = int(line[-1]) / 3600

    return spent


def DictToList(dict):
    """Convert a dictonary to list.

    return: x, y
    """
    names = []
    times = []
    for key in dict:
        names.append(key)
        times.append(dict[key])

    return names, times


def Plot(x, y, team, estTime=4):
    """
    Plot a graphic.

    x -> axis X
    y -> axis Y
    estimate time (default) -> 4h
    """
    plt.figure(1)
    plt.style.use("ggplot")

    plt.bar(x, y, label='Spent Time')
    plt.hlines(estTime, xmin=-1, xmax=len(x), linestyles='dashed',
               color='blue', label='Estimated Time')
    plt.legend(loc="upper left")
    plt.xlabel('Developers')
    plt.ylabel('Time (hours)')
    plt.xticks(rotation=20)
    plt.title(team + "'s Spent Time ")

    plt.show()


if __name__ == "__main__":
    args = sys.argv

    fileName = 'kahuc-kahuc_issues'
    sprint = 'Sprint'
    if fileName in args[1] and sprint in args[3] and len(args) == 4:

        try:
            team = args[2]
            time = ReadCsv(args[1], args[2], args[3])
            names, time = DictToList(time)
            Plot(names, time, team, 8)

        except:
            print("An error occured")

    else:
        print("Wrong parameters")
