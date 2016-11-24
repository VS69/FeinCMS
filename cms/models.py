# -*- coding: utf-8 -*-

from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent


Page.register_templates({
    'title': 'Основний темплейт FeinCMS',
    'path': 'template1.html',
    'regions': (
        ('header', 'Шапка'),
        ('main', 'Вміст'),
        ('sidebar', 'Сайдбар', 'inherited'),
        ('footer', 'Підвал'),
    ),
})

Page.create_content_type(RichTextContent)
