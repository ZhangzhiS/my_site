#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# @Author   : zhi
# @Time     : 2019/4/10 下午3:13
# @Filename : pages
# @Software : PyCharm


def get_page_index(page_number, content_number=10):
    """
    根据页数计算索引范围

    :param page_number: 页数
    :param content_number: 每页展示的内容数量
    :return: 元组,起始位置和结束位置
    """
    try:
        page_number = int(page_number)
    except TypeError:
        page_number = 1
    start_index = (page_number-1) * content_number
    end_index = start_index + content_number
    return start_index, end_index
