from django.contrib import admin

# Register your models here.

from exam_app import models

admin.site.register(models.Login)
admin.site.register(models.Student)
admin.site.register(models.Exams)