from django.urls import path
from . import views

urlpatterns = [
    path('', views.PdfLoverPage.as_view(), name='home-page'),
    path('convert-image-to-pdf/', views.ConvertImageToPdf.as_view(), name='image-to-pdf'),
    path('convert-word-to-pdf/', views.ConvertWordToPdf.as_view(), name='word-to-pdf'),
]