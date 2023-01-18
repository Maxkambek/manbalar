from django.db import models


class Docs(models.Model):
    work_name = models.CharField(max_length=333)
    author = models.CharField(max_length=120)
    calligrapher = models.CharField(max_length=221, null=True, blank=True)
    subject = models.CharField(max_length=222, blank=True, null=True)
    language = models.CharField(max_length=60, null=True, blank=True)
    date_write = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=220, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    inventor_id = models.PositiveIntegerField()
    format = models.CharField(max_length=100)
    place_saved = models.CharField(max_length=221)
    description = models.TextField()

    def __str__(self):
        return self.work_name

    class Meta:
        verbose_name = 'Tarixiy manbalar'
        verbose_name_plural = 'Tarixiy manbalar'


class Works(models.Model):
    work_name = models.CharField(max_length=333)
    author = models.CharField(max_length=120)
    calligrapher = models.CharField(max_length=221, null=True, blank=True)
    subject = models.CharField(max_length=222, blank=True, null=True)
    language = models.CharField(max_length=60, null=True, blank=True)
    date_write = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=220, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    inventor_id = models.PositiveIntegerField()
    format = models.CharField(max_length=100)
    place_saved = models.CharField(max_length=221)
    description = models.TextField()

    def __str__(self):
        return self.work_name

    class Meta:
        verbose_name = 'Asarlar'
        verbose_name_plural = 'Asarlar'


class Handbooks(models.Model):
    work_name = models.CharField(max_length=333)
    author = models.CharField(max_length=120)
    calligrapher = models.CharField(max_length=221, null=True, blank=True)
    subject = models.CharField(max_length=222, blank=True, null=True)
    language = models.CharField(max_length=60, null=True, blank=True)
    date_write = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=220, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    inventor_id = models.PositiveIntegerField()
    format = models.CharField(max_length=100)
    place_saved = models.CharField(max_length=221)
    description = models.TextField()

    def __str__(self):
        return self.work_name

    class Meta:
        verbose_name = "Qo'lyozmalar"
        verbose_name_plural = "Qo'lyozmalar"


class Lithography(models.Model):
    work_name = models.CharField(max_length=333)
    author = models.CharField(max_length=120)
    calligrapher = models.CharField(max_length=221, null=True, blank=True)
    subject = models.CharField(max_length=222, blank=True, null=True)
    language = models.CharField(max_length=60, null=True, blank=True)
    date_write = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=220, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    inventor_id = models.PositiveIntegerField()
    format = models.CharField(max_length=100)
    place_saved = models.CharField(max_length=221)
    description = models.TextField()

    def __str__(self):
        return self.work_name

    class Meta:
        verbose_name = 'Toshbosmalar'
        verbose_name_plural = 'Toshbosmalar'


class About(models.Model):
    name = models.CharField(max_length=221)
    text = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Loyiha haqida'
        verbose_name_plural = 'Loyiha haqida'


