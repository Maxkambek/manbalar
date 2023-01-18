from modeltranslation.translator import register, TranslationOptions
from .models import Docs, About, Lithography, Handbooks, Works


@register(About)
class AboutTrans(TranslationOptions):
    fields = ('name', 'text')


@register(Docs)
class DocsTrans(TranslationOptions):
    fields = ('work_name', 'author', 'calligrapher', 'subject', 'language', 'date_write', 'status', 'size', 'format',
              'place_saved', 'description')


@register(Lithography)
class LithTrans(TranslationOptions):
    fields = ('work_name', 'author', 'calligrapher', 'subject', 'language', 'date_write', 'status', 'size', 'format',
              'place_saved', 'description')


@register(Handbooks)
class HandTrans(TranslationOptions):
    fields = ('work_name', 'author', 'calligrapher', 'subject', 'language', 'date_write', 'status', 'size', 'format',
              'place_saved', 'description')


@register(Works)
class WorkTrans(TranslationOptions):
    fields = ('work_name', 'author', 'calligrapher', 'subject', 'language', 'date_write', 'status', 'size', 'format',
              'place_saved', 'description')
