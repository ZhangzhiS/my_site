import markdown
from django.http import JsonResponse
from django.shortcuts import render
from markdown.extensions.toc import TocExtension

from blog.models import Articles
from tools.pages import get_page_index

# Create your views here.
content_number = 10


def index(request):
    """
    首页
    """
    page = request.GET.get("page", 1)
    start, end = get_page_index(page_number=page, content_number=content_number)
    articles = Articles.objects.all().order_by("date")
    page_count = articles.count()
    this_page = articles[start: end]
    content = {
        "title": "首页",
        "articles": this_page,
        "previous": 0 if page == 1 else page - 1,
        "page": page,
        "next": 0 if this_page.count() < 10 else page + 1,
        "page_count": page_count
    }
    return render(request, "index.html", context=content)


def get_article(request):
    """
    博客详情页面
    """
    article_id = request.GET.get("article_id")
    article = Articles.objects.get(id=article_id)
    md = markdown.Markdown(
        extensions=[
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 目录扩展
            TocExtension(toc_depth=2)
        ]
    )
    article.contents = md.convert(article.contents)
    content = {
        "article": article,
        "toc": md.toc
    }
    return render(request, "article.html", context=content)




