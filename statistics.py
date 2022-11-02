

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

def plot_stats(content):

    count_dict = {key:0 for key in content[0].keys() if key != "Datum" and key != "Gastgeber"}
    for i in range(len(content)):
        for key in count_dict.keys():
            if content[i][key] == "x":
                count_dict[key] += 1

    plt.plot(list(count_dict.keys()), list(count_dict.values()), "ro")
    plt.ylabel("Teilgenommen x mal")
    plt.show()
    plt.plot(list(count_dict.keys()), list(count_dict.values()), "ro")
    plt.ylabel("Teilgenommen x mal")
    plt.savefig('statistics.png')


if __name__ == "__main__":

    content = read_csv("2022_Auswertung.csv")
    plot_stats(content)
