from django.db.models import QuerySet

from tabom.models import Article


def get_an_article(article_id: int) -> Article:
    article = Article.objects.filter(id=article_id).get()
    return article


def get_article_list(offset: int, limit: int) -> QuerySet[Article]:
    return Article.objects.order_by("-id").prefetch_related("like_set")[offset : offset + limit]
