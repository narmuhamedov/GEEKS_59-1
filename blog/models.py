from django.db import models




example_description = "Lorem Ipsum is simply dummy text of the printing and typesetting industry." \
" Lorem Ipsum has been the industry's standard dummy text ever since the 1500s," \
" when an unknown printer took a galley of type and scrambled it to make a type specimen book." \
" It has survived not only five centuries, but also the leap into electronic typesetting," \
" remaining essentially unchanged. It was popularised in the 1960s with the release of " \
"Letraset sheets containing Lorem Ipsum passages," \
" and more recently with desktop publishing software like Aldus " \
"PageMaker including versions of Lorem Ipsum."


CATEGORY_NEWS = (
    ('Колледжи', 'Колледжи'),
    ('IT', 'IT'),
    ('Курсы', 'Курсы'),
    ('ВУЗЫ', 'ВУЗЫ')

)

class NewsPost(models.Model):
    title = models.CharField(max_length=100, verbose_name='укажите название новости')
    photo = models.ImageField(upload_to='news/', verbose_name='загрузите основное фото')
    photo2 = models.ImageField(upload_to='news/', verbose_name='загрузите доп фото', blank=True)
    descpition = models.TextField(verbose_name='Укажите описание новости', default=example_description)
    category_news = models.CharField(max_length=100, choices=CATEGORY_NEWS, default='IT')
    url_news = models.URLField(verbose_name="вставьте ссылку с YOUTUBE", blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

#null=tru нужен для изменения название полей  
# для добавления нового поля, 
# для изменения старого поля
#после миграций

    class Meta:
        verbose_name = 'новый блог'
        verbose_name_plural = 'новости об IT'
    
    def __str__(self):
        return f'{self.title}:{self.created_at}'

#Один ко многим
class Reviews(models.Model):
    choice_post = models.ForeignKey(NewsPost, on_delete=models.CASCADE,  
                                    related_name='review')
    MARKS = (
        ('❤️', '❤️'),
        ('❤️❤️', '❤️❤️'),
        ('❤️❤️❤️', '❤️❤️❤️'),
        ('❤️❤️❤️❤️', '❤️❤️❤️❤️'),
        ('❤️❤️❤️❤️❤️', '❤️❤️❤️❤️❤️'),
    )
    marks = models.CharField(max_length=100, choices=MARKS, default='❤️❤️❤️❤️')
    text = models.TextField(verbose_name='Напишите отзыв')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_post}-{self.marks}'






class Slider(models.Model):
    image = models.URLField(verbose_name='вставьте ссылки с картинок GOOGLE')


    class Meta:
        verbose_name = 'картинку'
        verbose_name_plural = 'картинки'
        