from rest_framework.views import APIView, Response
from trip.common.request_utils import get_request_field
from trip.routes.tasks import create_route, find_best_route
from trip.common.exceptions import RouteException


class RouteAPIView(APIView):
    def get(self, request):
        source = get_request_field(request.query_params,
                                   "source",
                                   optional=False)
        destination = get_request_field(request.query_params,
                                        "destination",
                                        optional=False)
        try:
            cost, route = find_best_route(source, destination)
        except RouteException as e:
            return Response({"error": str(e)}, status=400)
        return Response({"route": route, "cost": cost}, status=200)

    def post(self, request):
        source = get_request_field(request.data, "source", optional=False)
        destination = get_request_field(request.data,
                                        "destination",
                                        optional=False)
        cost = str(get_request_field(request.data, "cost", optional=False))
        try:
            create_route(source, destination, cost)
        except RouteException as e:
            return Response({"error": str(e)}, status=400)
        return Response({"message": "New route successfully registered"},
                        status=200)
