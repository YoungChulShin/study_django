from django.contrib import admin
from django.urls import path
from book_api.views import book_list

urlpatterns = [
    path('list/', book_list)
]