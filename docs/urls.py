from django.urls import path
from . import views

urlpatterns = [
    path('about-project/', views.AboutListAPIView.as_view()),
    path('docs-history/', views.DocListAPIView.as_view()),
    path('lithography/', views.LithListAPIView.as_view()),
    path('works/', views.WorkListAPIView.as_view()),
    path('handbooks/', views.HandListAPIView.as_view()),
    path('docs-history/<int:pk>/', views.DocsDetailAPIView.as_view()),
    path('lithography/<int:pk>/', views.LithDetailAPIView.as_view()),
    path('works/<int:pk>/', views.WorkDetailAPIView.as_view()),
    path('handbooks/<int:pk>/', views.HandDetailAPIView.as_view()),
    path('statistics/', views.StatisticsAPIView.as_view())
]
