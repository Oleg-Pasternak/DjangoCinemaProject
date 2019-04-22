from rest_framework.generics import ListAPIView
from cinema.models import Movie
from cinema_api.serializers import MovieSerializer
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 25


class TestView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = StandardResultsSetPagination

    # def get(self, request):
    #     result = {"films": list()}
    #     for movie in Movie.objects.all():
    #         result["films"].append({"title": movie.title})
    #     return Response(result, status=200)
