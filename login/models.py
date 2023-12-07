# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Manager(models.Model):
    id = models.AutoField(primary_key=True, db_comment='管理员编号', db_column='manager_id')
    mname = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True,
                             db_comment='管理员名字')
    username = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True,
                                db_comment='联系方式', db_column='phone')
    password = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True, db_comment='密码')
    photo = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True, db_comment='照片')
    days = models.CharField(max_length=10, db_collation='utf8_general_ci', blank=True, null=True, db_comment='到店天数')
    address = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True,
                               db_comment='现居地')
    restrict = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True, db_comment='权限')
    sex = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True, db_comment='性别')
    age = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True, db_comment='年龄')
    stage = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True, db_comment='状态')
    date = models.DateField(blank=True, null=True, db_comment='入职日期')

    # identifier = models.CharField(max_length=40, unique=True)
    # USERNAME_FIELD = 'identifier'
    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    class Meta:
        managed = False
        db_table = 'manager'
