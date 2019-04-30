import os
from trip.common.csv_utils import write_line_to_csv, read_csv_content
from trip.common.exceptions import ValdationError, RouteException
from trip.routes.algorithm import dijkstra

CSV_FILENAME = lambda : os.getenv("CSV_FILENAME", "input-file.csv")


def create_route(source, destination, cost):
    source, destination = source.upper(), destination.upper()
    if len(source) != 3 or len(destination) != 3:
        raise ValdationError(
            "Airports should have only 3 letters, Trying to add: %s -> %s"
            % (source, destination))

    if not cost.isdigit():
        raise ValdationError("Invalid cost %s for route" % cost)

    for i, datapoint in enumerate(read_csv_content(CSV_FILENAME())):
        if datapoint[0] == source and datapoint[1] == destination:
            raise ValdationError("There is already a cost for this route")

    write_line_to_csv(CSV_FILENAME(), [source, destination, cost])


def find_best_route(source, destination):
    source, destination = source.upper(), destination.upper()
    response = dijkstra(read_csv_content(CSV_FILENAME()), source, destination)
    if not response:
        raise RouteException("There is no possible route between these airports")
    cost, route_tuple = response[0], response[1]
    parsed_route = parse_algorithm_response(route_tuple)
    return cost, parsed_route


def parse_algorithm_response(route_tuple):
    parsed_route = []
    while (route_tuple[1]):
        parsed_route.append(route_tuple[0])
        route_tuple = route_tuple[1]
    parsed_route.append(route_tuple[0])
    parsed_route.reverse()
    return parsed_route
