#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.contrib import admin
from login.models import Manager


# Register your models here.

class ManagerModelAdmin(admin.ModelAdmin):
    list_display = (
        'manager_id',
        'mname',
        'phone',
        'password',
        'photo',
        'days',
        'address',
        'restrict',
        'sex',
        'age',
        'stage',
        'date',
    )
    search_fields = ('name',)
    ordering = ('manager_id',)


admin.site.register(Manager, ManagerModelAdmin)
