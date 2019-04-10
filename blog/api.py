#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# @Author   : zhi
# @Time     : 2019/4/10 下午4:27
# @Filename : api
# @Software : PyCharm
from django.http import JsonResponse
from blog.models import Articles, Tags
from django.forms.models import model_to_dict


def get_newest(request):
    """
    异步加载最新文章
    """
    articles = Articles.objects.order_by("-date")[:3]
    newest_articles = []
    for article in articles:
        temp = model_to_dict(article)
        newest_articles.append(temp)
    return JsonResponse(newest_articles, safe=False)


def get_tags(request):
    """
    异步加载所有标签
    """
    tags = Tags.objects.all()
    tags_list = []
    for tag in tags:
        tags_list.append(tag.tag_name)
    return JsonResponse(tags_list, safe=False)