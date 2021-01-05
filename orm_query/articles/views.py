from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template_name = 'articles/news.html'

    articles_query = Article.objects.all().defer('published_at').select_related('author').select_related('genre')

    context = {
        'object_list': articles_query
    }

    return render(request, template_name, context)
