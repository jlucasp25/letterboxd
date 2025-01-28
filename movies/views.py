from django.views.generic import TemplateView, ListView

from movies.models import Movie


class IndexView(TemplateView):
    template_name = 'index.html'


class TitleMixin:
    title = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context


class MovieListView(TitleMixin, ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movies'
    title = "All Movies"

    def get_queryset(self):
        qs = super().get_queryset()
        genre = self.request.GET.get('genre', None)
        if genre:
            qs = qs.filter(genre__name=genre)
            self.title = f"{genre} Movies"
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] = Movie.objects.values_list('genre__name', flat=True).distinct()
        return context


class AnimationMovieListView(TitleMixin, ListView):
    queryset = Movie.objects.filter(genre__name='Animation')
    template_name = 'movie_list.html'
    context_object_name = 'movies'
    title = "Animation Movies"
