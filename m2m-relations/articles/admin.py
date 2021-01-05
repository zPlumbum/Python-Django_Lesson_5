from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleTag


class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_exists = False
        is_main_counter = 0

        for form in self.forms:
            if form.cleaned_data:
                if form.cleaned_data['is_main']:
                    is_main_exists = True
                    is_main_counter += 1

            if not is_main_exists:
                raise ValidationError('Нужно выбрать основной тег')
            if is_main_counter > 1:
                raise ValidationError('Основным может быть только один тег')

        return super().clean()


class ArticleTagInLine(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ArticleTagInLine
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
