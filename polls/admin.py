from django.contrib import admin

# Register your models here.

from django.contrib import admin

from polls.models import TbSubject, TbTeacher


class TbSubjectModelAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'intro', 'is_hot')
    search_fields = ('name',)
    ordering = ('no',)


class TbTeacherModelAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'sex', 'birth', 'intro','photo','gcount', 'bcount', 'sno')
    search_fields = ('name',)
    ordering = ('no',)


admin.site.register(TbSubject, TbSubjectModelAdmin)
admin.site.register(TbTeacher, TbTeacherModelAdmin)
