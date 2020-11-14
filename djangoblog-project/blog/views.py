# from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from hitcount.views import HitCountDetailView

from .models import Artigo


# Create your views here.

class IndexView(ListView):
    model = Artigo
    context_object_name = 'artigos'
    template_name = 'index.html'


class ArtigoDetailView(HitCountDetailView):
    model = Artigo
    template_name = 'artigo_detalhe.html'
    context_object_name = 'artigo'
    slug_field = 'slug'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(ArtigoDetailView, self).get_context_data(**kwargs)
        context.update({
            'popular_posts': Artigo.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context
