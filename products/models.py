from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

description_ex = "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, "

class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default=description_ex)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}----{", ".join(i.name for i in self.categories.all() )}"

    # Шашлык - #еда, #Грузия, #говядина