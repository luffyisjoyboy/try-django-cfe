from django.test import TestCase

# Create your tests here.
from .models import Article
from django.utils.text import slugify

from .utils import slugify_instance_title

class ArticleTestCase(TestCase):
    def setUp(self):
        self.no_of_articles=5
        for i in range(0, self.no_of_articles):
            Article.objects.create(title='hello world', content='something else')

    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), self.no_of_articles)
    
    def test_hello_world(self):
        obj = Article.objects.all().order_by("id").first()
        slug = obj.slug
        self.assertEqual(slug, slugify(obj.title))

    def test_hello_world_unique_slug(self):
        qs = Article.objects.all().exclude(slug__iexact='hello-world')
        for obj in qs:
            slug = obj.slug
            self.assertNotEqual(slug, slugify(obj.title))
    
    def test_slugify_instance_title(self):
        obj = Article.objects.all().last()
        new_slug = []
        for i in range(0, 5):
           instance = slugify_instance_title(obj)
           new_slug.append(instance.slug)
        unique_slugs = list(set(new_slug))
        self.assertEqual(len(new_slug), len(unique_slugs))

    def test_slugify_instance_title_redux(self):
        slug_list = Article.objects.all().values_list('slug', flat=True)
        unique_slug_list = list(set(slug_list))
        self.assertEqual(len(slug_list), len(unique_slug_list))

    def test_article_search_manager(self):
        qs = Article.objects.search(query='hello world')
        self.assertEqual(qs.count(), self.no_of_articles)

        qs1 = Article.objects.search(query='hello')
        self.assertEqual(qs1.count(), self.no_of_articles)

        qs2 = Article.objects.search(query='world')
        self.assertEqual(qs2.count(), self.no_of_articles)

