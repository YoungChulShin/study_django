from django.db import models

# Create your models here.
class Book(models.Model): 
    title = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()

    # Object의 문자열을 리턴하는 클래스
    def __str__(self):
        return self.title