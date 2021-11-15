from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime



# Создаём модель товара 
class New(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=64, unique=True, default = "Default value")
    
    category = models.ForeignKey(to='Category',on_delete=models.CASCADE,related_name='news')


    def __str__(self):
        return f'{self.name.title()}: {self.description[:40]}'
    
    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'

#  создаём категорию, к которой будет привязываться товар
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # названия категорий тоже не должны повторяться
 
    def __str__(self):
        return f'{self.name.title()}'



