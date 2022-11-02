

import matplotlib.pyplot as plt


def read_csv(path_to_csv):

    with open(path_to_csv, "r") as csv_file:
        lines = csv_file.readlines()
        header = lines[0].split(";")
        content = []
        for line in lines[1:]:
            cell_dict = {}
            cells = line.split(";")
            for i in range(len(cells)):
                cell_dict[header[i].strip()] = cells[i].strip()
            content.append(cell_dict)                

    return content


def get_stats(content):
    count_dict = {key:0 for key in content[0].keys() if key != "Datum" and key != "Gastgeber"}
    for i in range(len(content)):
        for key in count_dict.keys():
            if content[i][key] == "x":
                count_dict[key] += 1
    return count_dict


def plot_stats(count_dict, mode = "plot"):

    plt.plot(list(count_dict.keys()), list(count_dict.values()), "ro")
    plt.title("Stammtisch-Statistik")
    plt.ylabel("Teilgenommen x mal")
    plt.yticks([i for i in range(0, max(count_dict.values()) + 1)])
    plt.grid()
    if mode == "plot":
        plt.show()
    elif mode == "save":
        plt.savefig('statistics.png')


if __name__ == "__main__":

    content     = read_csv("2022_Auswertung.csv")
    count_dict  = get_stats(content)

    plot_stats(count_dict, "plot")
    plot_stats(count_dict, "save")
