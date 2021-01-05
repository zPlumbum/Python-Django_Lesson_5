from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    tags = models.ManyToManyField('Tag', related_name='to_article', blank=True, through='ArticleTag')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return f'{self.title}'


class ArticleTag(models.Model):
    article = models.ForeignKey(Article, related_name='tags_to_article', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='articles_for_tag', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной')

    def __str__(self):
        return f'Статья - {self.article}, тэг: {self.tag}, основной: {self.is_main}'
