from django.core.management.base import BaseCommand
from trip.routes.tasks import create_route, find_best_route


def option(command_description, actions={}):
    action = input(command_description)
    if not actions:
        return action
    try:
        actions[action]()
    except KeyError:
        print("Opção inexistente.")
        exit()


def create_route_cli():
    src = option("Origem (Ex: GRU): ")
    dest = option("Destino (Ex: ORL): ")
    cost = option("Defina um custo (Ex: 1,2,3...): ")
    try:
        create_route(src, dest, cost)
        print("Rota criada com sucesso")
    except Exception as e:
        print("Nâo foi possível criar rota: %s" % str(e))


def find_best_route_cli():
    route = option("Rota (Ex: GRU-CDG): ")
    try:
        splitted_route = route.split("-")
        src, dest = splitted_route[0], splitted_route[1]
        try:
            cost, best_route = find_best_route(src, dest)
            print("Melhor rota: %s com custo de %s" %
                  (" -> ".join(best_route), cost))
        except Exception as e2:
            print("Nâo foi possível criar rota: %s" % str(e2))
    except Exception:
        print("Nâo foi possível entener a rota rota: %s" % route)


class Command(BaseCommand):
    def handle(self, *args, **options):
        option(
            "1 - Achar melhor rota entre 2 aeroportos\n" +
            "2 - Criar nova rota\nEscolha uma ação: ", {
                "1": find_best_route_cli,
                "2": create_route_cli,
                "um": find_best_route_cli,
                "dois": create_route_cli,
                "Um": find_best_route_cli,
                "Dois": create_route_cli
            })
