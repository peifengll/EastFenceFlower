#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TbSubject(models.Model):
    no = models.AutoField(primary_key=True, db_comment='学科编号')
    name = models.CharField(max_length=50, db_comment='学科名称')
    intro = models.CharField(max_length=1000, db_comment='学科介绍')
    is_hot = models.IntegerField(db_comment='是不是热门学科')

    def __str__(self):
        return "{}->({}).{},{}".format(self.__class__.__name__, self.name, self.intro, self.is_hot)

    class Meta:
        managed = False
        db_table = 'tb_subject'


class TbTeacher(models.Model):
    no = models.AutoField(primary_key=True, db_comment='老师编号')
    name = models.CharField(max_length=20, db_comment='老师姓名')
    sex = models.IntegerField(db_comment='老师性别')
    birth = models.DateField(db_comment='出生日期')
    intro = models.CharField(max_length=1000, db_comment='老师介绍')
    photo = models.CharField(max_length=255, db_comment='老师照片')
    gcount = models.IntegerField(db_comment='好评数')
    bcount = models.IntegerField(db_comment='差评数')
    sno = models.ForeignKey(TbSubject, models.DO_NOTHING, db_column='sno', db_comment='所属学科')

    class Meta:
        managed = False
        db_table = 'tb_teacher'
