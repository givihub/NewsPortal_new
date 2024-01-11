from .models import Category
from modeltranslation.translator import register, \
    TranslationOptions

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name_category',)  # указываем, какие именно поля надо переводить в виде кортежа