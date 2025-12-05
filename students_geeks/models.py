from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='введите имя студента')
    third_name = models.CharField(max_length=100, verbose_name='введите отчество', blank=True)
    age = models.PositiveIntegerField(default=17, verbose_name='введите возраст')
    certificate = models.FileField(upload_to='documents/', verbose_name='загрузите аттестат')
    ORT_test = models.URLField(verbose_name='загрузите результат ORT')

    DIRECTIONS = (
        ('Backend', 'Backend'),
        ('Frontend', 'Frontend'),
        ('UX-UI', "UX-UI"),
        ('Не определился(ась)', 'Не определился(ась)')
    )
    directions = models.CharField(max_length=100, choices=DIRECTIONS, default='Backend', 
                                  verbose_name='выберите направление')
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name}:{self.directions}'
    
    class Meta:
        verbose_name = 'студента'
        verbose_name_plural= 'студенты'