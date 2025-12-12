from django.db import models

class Car(models.Model):
    title_car = models.CharField(max_length=100, verbose_name='введите название машины')
    name_driver = models.CharField(max_length=100, verbose_name='укажите имя водителя', default='Иван')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_car

class NummerCar(models.Model):
    choice_car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='nummer_car')
    number_car = models.CharField(verbose_name='придумайте номер машины', max_length=100, default='--KG------')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_car}-{self.number_car}'