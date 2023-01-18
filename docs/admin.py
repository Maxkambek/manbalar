from django.contrib import admin
from .models import About, Docs, Handbooks, Works, Lithography
from modeltranslation.admin import TranslationAdmin


class AboutAdmin(TranslationAdmin):
    pass


class DocAdmin(TranslationAdmin):
    pass


class HandAdmin(TranslationAdmin):
    pass


class WorkAdmin(TranslationAdmin):
    pass


class LithAdmin(TranslationAdmin):
    pass


admin.site.register(About, AboutAdmin)
admin.site.register(Docs, DocAdmin)
admin.site.register(Handbooks, HandAdmin)
admin.site.register(Works, WorkAdmin)
admin.site.register(Lithography, LithAdmin)
