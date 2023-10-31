from modeltranslation.translator import TranslationOptions, translator

from course.models import Course, CourseContent, CourseSection


class CourseTranslationOptions(TranslationOptions):
    fields = ("name", "desc")


class CourseContentTranslationOptions(TranslationOptions):
    fields = ("title", "description", "section")


class CourseSectionTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(Course, CourseTranslationOptions)
translator.register(CourseSection, CourseSectionTranslationOptions)
translator.register(CourseContent, CourseContentTranslationOptions)
