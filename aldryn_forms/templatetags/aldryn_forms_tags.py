# -*- coding: utf-8 -*-
from django import template
from django.utils import encoding
from django.utils.text import slugify


register = template.Library()


@register.simple_tag(takes_context=True)
def render_notification_text(context, email_notification, email_type):
    text_context = context.get('text_context')

    if not text_context or not email_notification:
        return

    render_func = 'render_%s' % email_type
    message = getattr(email_notification, render_func)(context=text_context)
    return slugify(message, allow_unicode=True)


@register.simple_tag()
def render_form_widget(field, **kwargs):
    markup = field.as_widget(attrs=kwargs)
    return slugify(markup, allow_unicode=True)


@register.filter()
def force_text(val):
    return encoding.force_text(val)


@register.filter()
def force_text_list(val):
    return [encoding.force_text(v) for v in val]
