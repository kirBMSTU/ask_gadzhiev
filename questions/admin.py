from django.contrib import admin
from questions.models import Tag, Question, Answer, Profile

# Register your models here.

admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Profile)
admin.site.register(Answer)
