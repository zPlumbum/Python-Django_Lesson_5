from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'

    articles_query = Article.objects.all().prefetch_related('tags_to_article').order_by('-published_at')

    context = {
        'object_list': articles_query
    }

    return render(request, template, context)
