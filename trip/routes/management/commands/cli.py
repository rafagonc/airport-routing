import os
from django.core.management.base import BaseCommand
from trip.routes.tasks import create_route, find_best_route


def option(command_description, actions={}):
    action = input(command_description)
    if not actions:
        return action
    try:
        actions[action]()
    except KeyError:
        print("Unexisting option for this value.")
        exit()


def create_route_cli():
    src = option("Source (Ex: GRU): ")
    dest = option("Destination (Ex: ORL): ")
    cost = option("Cost (Ex: 1,2,3...): ")
    try:
        create_route(src, dest, cost)
        print("New route successfully registered")
    except Exception as e:
        print("Cannot create route: %s" % str(e))


def find_best_route_cli():
    route = option("Route (Ex: GRU-CDG): ")
    try:
        splitted_route = route.split("-")
        src, dest = splitted_route[0], splitted_route[1]
        try:
            cost, best_route = find_best_route(src, dest)
            print("Best route: %s with cost of %s" %
                  (" -> ".join(best_route), cost))
        except Exception as e2:
            print("Cannot find best route: %s" % str(e2))
    except Exception:
        print("Cannot parse route: %s" % route)


class Command(BaseCommand):
    def handle(self, *args, **options):
        filename = options['filename']
        os.environ["CSV_FILENAME"] = filename
        option(
            "1 - Best route between 2 airports\n" +
            "2 - Create new route\nChoose an action: ", {
                "1": find_best_route_cli,
                "2": create_route_cli,
                "um": find_best_route_cli,
                "dois": create_route_cli,
                "Um": find_best_route_cli,
                "Dois": create_route_cli
            })

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)
