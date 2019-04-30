from trip.common.csv_utils import write_line_to_csv, read_csv_content
from trip.common.exceptions import ValdationError
from trip.routes.algorithm import dijkstra

CSV_FILENAME = "input-file.csv"


def create_route(source, destination, cost):
    if len(source) != 3 or len(destination) != 3:
        raise ValdationError(
            "Aeroportos devem ter 3 letras somente! Tentativa de adicionar: %s -> %s"
            % (source, destination))

    if not cost.isdigit():
        raise ValdationError("Custo %s inválido para rota" % cost)

    write_line_to_csv(CSV_FILENAME, [source, destination, cost])


def find_best_route(source, destination):
    response = dijkstra(read_csv_content(CSV_FILENAME), source, destination)
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
