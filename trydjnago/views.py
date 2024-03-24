import random
from django.http import HttpResponse
from articles.models import Article

from django.template.loader import render_to_string

def home_view(request):

    name = 'Batman'
    number  = 18
    article_obj = Article.objects.get(id=number)
    article_queryset = Article.objects.all()
    content = {
        'object': article_obj,
        'object_list': article_queryset,
    }
    html_string = render_to_string('home_view.html', context=content)
    return HttpResponse(html_string)