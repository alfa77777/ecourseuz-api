from modeltranslation.translator import TranslationOptions, translator

from common.models import AboutUsFull


class AboutUsFullTranslationOptions(TranslationOptions):
    fields = ("name", "text")


translator.register(AboutUsFull, AboutUsFullTranslationOptions)
