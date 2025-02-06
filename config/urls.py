"""
URL configuration for letterboxd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from movies.views import IndexView, MovieListView, AnimationMovieListView, MovieCreateView, MovieUpdateView, \
    MovieDeleteView, MovieDetailView, ContactView

urlpatterns = [
    path("xpto/", admin.site.urls),
    path("", IndexView.as_view()),
    path("movies/", MovieListView.as_view(), name="movie-list"),
    path("movies-animation/", AnimationMovieListView.as_view(), name="animation-movie-list"),
    path("movies-create/", MovieCreateView.as_view(), name="movie-create"),
    path("movies-update/<int:pk>/", MovieUpdateView.as_view(), name="movie-update"),
    path("movies-delete/<int:pk>/", MovieDeleteView.as_view(), name="movie-delete"),
    path("movies-detail/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("contact-success/", TemplateView.as_view(template_name="contact_success.html"), name="contact-success"),
    path("api/", include("movies.api.urls")),
]
