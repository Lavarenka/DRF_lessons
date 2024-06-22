from django.db import models


class Post(models.Model):
    """
    auto_now_add / заполняется автоматом только после создания
    auto_now / заполняется автоматом после каждого сохранения
    посмотреть filefild
    """

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    photo_preview = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото_превтю')
    photo_post = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото_статьи')
    photo_header = models.ImageField(upload_to='photos_header', blank=True, verbose_name='Фото_фон')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    number_series = models.IntegerField(default=1, verbose_name='Номер книги серии')
    genre = models.ManyToManyField('Genre', related_name='genre', verbose_name='Жанры')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass

    class Meta:
        ordering = ['title']
        verbose_name = 'Жанр'  # название блога в админке
        verbose_name_plural = 'Жанры'  # название блога в админке во множественном числе
