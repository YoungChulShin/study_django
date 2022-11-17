from django.contrib import admin
from django.urls import path
from book_api.views import BookList

urlpatterns = [
    # path('', book_create),
    # path('list/', book_list),
    # path('<int:pk>', book),

    path('list/', BookList.as_view()),
]