from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView, FormView

from movies.forms import ContactForm
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


class MovieCreateView(CreateView):
    model = Movie
    fields = ['title', 'year', 'genre']
    template_name = 'movie_create_update.html'
    success_url = reverse_lazy("movie-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = "Create Movie"
        return context


class MovieUpdateView(UpdateView):
    model = Movie
    fields = ['title', 'year', 'genre']
    template_name = 'movie_create_update.html'
    success_url = reverse_lazy("movie-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = "Update Movie"
        return context


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy("movie-list")


class MovieDetailView(DetailView):
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["detail"] = True
        return context


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact-success")

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)