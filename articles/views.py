from django.shortcuts import render, redirect
from .models import Article
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

# Create your views here.
@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        'article_obj': None,
        'created': False,
        'form': form
    }

    if form.is_valid():
        article_obj = form.save()
        context['form'] = ArticleForm()
        return redirect(article_obj.get_absolute_url())
        # return redirect("article-detail", slug=article_obj.slug)
        # return redirect(article_obj.get_absolute_url())
    
    return render(request, 'articles/create.html', context=context)


def article_search_view(request):
    query = request.GET.get('q')
    qs = Article.objects.search(query=query)
    context = {
        'obj_list': qs
    }
    return render(request, 'articles/search.html',context=context)

# Create your views here.
def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        "article_obj": article_obj,
    }
    return render(request, "articles/detail.html", context=context)