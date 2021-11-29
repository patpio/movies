from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from movies.models import Movie


class MoviesListView(ListView):
    model = Movie
    template_name = 'movies/movies_list.html'
    context_object_name = 'movies'


class MoviesDetailView(DetailView):
    model = Movie
    template_name = 'movies/movies_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actors'] = self.object.actors.all()
        context['categories'] = self.object.type.all()
        return context


class MoviesCreateView(CreateView):
    model = Movie
    fields = '__all__'
    template_name = 'movies/movies_create.html'
    success_url = reverse_lazy('movies:list')


class MoviesUpdateView(UpdateView):
    model = Movie
    fields = '__all__'
    template_name = 'movies/movies_update.html'

    def get_success_url(self):
        return reverse_lazy('movies:detail', kwargs={'pk': self.object.pk})


class MoviesDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy('movies:list')
