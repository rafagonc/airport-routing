import csv
from trip.common.exceptions import MissingFileException, ValdationError


def write_line_to_csv(filename, content):
    try:
        with open(filename, "a") as csvfile:
            csvfile.write("\n" + ",".join(content))
    except FileNotFoundError:
        raise MissingFileException(filename)


def read_csv_content(filename):
    try:
        data = []
        with open(filename, "r+") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                data.append((row[0], row[1], int(row[2])))
        return data
    except FileNotFoundError:
        raise MissingFileException(filename)
