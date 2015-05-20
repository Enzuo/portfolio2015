from modeltranslation.translator import translator, TranslationOptions
from portfolio.models import Work, Article, Tag

class WorkTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
    
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
    
class TagTranslationOptions(TranslationOptions):
	fields = ('name',)


translator.register(Work, WorkTranslationOptions)
translator.register(Article, ArticleTranslationOptions)
translator.register(Tag, TagTranslationOptions)

'''
Rule 1

    Reading the value from the original field returns the value translated to the current language.

Rule 2

    Assigning a value to the original field updates the value in the associated current language translation field.

Rule 3

    If both fields - the original and the current language translation field - are updated at the same time, the current language translation field wins.
'''
