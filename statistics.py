

import matplotlib.pyplot as plt
import pandas as pd

def read_csv(path_to_csv):

    with open(path_to_csv, "r") as csv_file:
        lines = csv_file.readlines()
        raw_content = []
        for line in lines:
            raw_content.append([l.strip() for l in line.split(";")])
        header = lines[0].split(";")
        content = []
        for line in lines[1:]:
            cell_dict = {}
            cells = line.split(";")
            for i in range(len(cells)):
                cell_dict[header[i].strip()] = cells[i].strip()
            content.append(cell_dict)                

    return content, raw_content


def get_stats(content):
    count_dict = {key:0 for key in content[0].keys() if key != "Datum" and key != "Gastgeber"}
    for i in range(len(content)):
        for key in count_dict.keys():
            if content[i][key] == "x":
                count_dict[key] += 1
    return count_dict


def plot_stats(count_dict, mode = "plot"):

    plt.bar(list(count_dict.keys()), list(count_dict.values()), width=0.4)
    plt.title("Stammtisch-Statistik")
    plt.ylabel("Teilgenommen x mal")
    plt.yticks([i for i in range(0, max(count_dict.values()) + 1)])
    if mode == "plot":
        plt.show()
    elif mode == "save":
        plt.savefig('statistics.png')
    plt.cla()

def plot_map(content, mode):

    names = [n for n in content[0][2:]]
    dates = [d[0] for d in content[1:]]
    values = []
    for c in content[1:]:
        values.append([1 if i=="x" else 0 for i in c[2:]])
    plt.imshow( values , cmap = 'RdYlGn')
    plt.xticks(range(len(names)), names)
    plt.yticks(range(len(dates)), dates)
    if mode == "plot":
        plt.show()
    elif mode == "save":
        plt.savefig('map.png')
    plt.cla()


if __name__ == "__main__":

    content, raw_content = read_csv("2022_Auswertung.csv")
    count_dict  = get_stats(content)

    #plot_stats(count_dict, "plot")
    plot_stats(count_dict, "save")
    #plot_map(raw_content, "plot")
    plot_map(raw_content, "save")