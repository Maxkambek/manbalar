from rest_framework import serializers
from .models import Lithography, Docs, Handbooks, Works, About


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'name', 'text']


class HandbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handbooks
        fields = ['id', 'work_name', 'author', 'calligrapher', 'subject', 'language', 'date_write', 'status', 'size',
                  'format', 'place_saved', 'description', 'inventor_id']


class DocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docs
        fields = ['id', 'work_name', 'author', 'calligrapher', 'subject', 'language', 'date_write', 'status', 'size',
                  'format', 'place_saved', 'description', 'inventor_id']


class WorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = ['id', 'work_name', 'author', 'calligrapher', 'subject', 'language', 'date_write', 'status', 'size',
                  'format', 'place_saved', 'description', 'inventor_id']


class LithSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lithography
        fields = ['id', 'work_name', 'author', 'calligrapher', 'subject', 'language', 'date_write', 'status', 'size',
                  'format', 'place_saved', 'description', 'inventor_id']


class HandDetailBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handbooks
        fields = ['id', 'work_name', 'author', 'date_write']


class DocsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docs
        fields = ['id', 'work_name', 'author', 'date_write']


class WorksDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = ['id', 'work_name', 'author', 'date_write']


class LithDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lithography
        fields = ['id', 'work_name', 'author', 'date_write']
