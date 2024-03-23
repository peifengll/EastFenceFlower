#!/user/bin/env python3
# -*- coding: utf-8 -*-

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    add_id = models.AutoField(primary_key=True, db_comment='地址编号')
    uname = models.CharField(max_length=50, blank=True, null=True, db_comment='姓名')
    phone = models.CharField(max_length=50, blank=True, null=True, db_comment='联系方式')
    address = models.CharField(max_length=255, blank=True, null=True, db_comment='地址')
    u_id = models.IntegerField(blank=True, null=True, db_comment='用户编号')

    class Meta:
        managed = False
        db_table = 'address'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True, db_comment='购物车编号')
    uname = models.CharField(max_length=50, blank=True, null=True, db_comment='用户名')
    user_id = models.CharField(max_length=50, blank=True, null=True, db_comment='用户编号')
    gname = models.CharField(max_length=50, blank=True, null=True, db_comment='商品名')
    goods_id = models.CharField(max_length=50, blank=True, null=True, db_comment='商品编号')
    num = models.CharField(max_length=50, blank=True, null=True, db_comment='数量')
    price = models.CharField(max_length=50, blank=True, null=True, db_comment='价格')
    size = models.CharField(max_length=50, blank=True, null=True, db_comment='大中小')

    class Meta:
        managed = False
        db_table = 'cart'


class Date(models.Model):
    date_id = models.AutoField(primary_key=True, db_comment='日程编号')
    tab = models.CharField(max_length=50, blank=True, null=True, db_comment='标签')
    date = models.DateField(blank=True, null=True, db_comment='日期')
    event = models.CharField(max_length=50, blank=True, null=True, db_comment='事件')
    spot = models.CharField(max_length=50, blank=True, null=True, db_comment='地点')
    time = models.TimeField(blank=True, null=True, db_comment='时间')

    class Meta:
        managed = False
        db_table = 'date'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Flower(models.Model):
    flower_id = models.AutoField(primary_key=True, db_comment='花编号')
    fname = models.CharField(max_length=50, blank=True, null=True, db_comment='花名')
    enname = models.CharField(max_length=50, blank=True, null=True, db_comment='英语名字')
    num = models.CharField(max_length=50, blank=True, null=True, db_comment='库存数量')
    sort = models.CharField(max_length=50, blank=True, null=True, db_comment='分类')
    feed = models.CharField(max_length=255, blank=True, null=True, db_comment='养殖方式')
    nickname = models.CharField(max_length=50, blank=True, null=True, db_comment='别名')
    ldname = models.CharField(max_length=50, blank=True, null=True, db_comment='拉丁名')
    brithplace = models.CharField(max_length=50, blank=True, null=True, db_comment='原产地')
    enplace = models.CharField(max_length=50, blank=True, null=True, db_comment='英文地名')
    image = models.CharField(max_length=255, blank=True, null=True, db_comment='图片')
    image2 = models.CharField(max_length=255, blank=True, null=True, db_comment='图片2')
    image3 = models.CharField(max_length=255, blank=True, null=True, db_comment='图片3')
    use = models.CharField(max_length=255, blank=True, null=True, db_comment='用途')
    intor = models.TextField(blank=True, null=True, db_comment='介绍')
    temp = models.CharField(max_length=50, blank=True, null=True, db_comment='温度')
    water = models.CharField(max_length=50, blank=True, null=True, db_comment='水分')
    light = models.CharField(max_length=50, blank=True, null=True, db_comment='光照')
    season = models.CharField(max_length=50, blank=True, null=True, db_comment='季节')
    manure = models.CharField(max_length=50, blank=True, null=True, db_comment='肥料')
    soil = models.CharField(max_length=50, blank=True, null=True, db_comment='土壤')
    lop = models.CharField(max_length=50, blank=True, null=True, db_comment='修剪')

    class Meta:
        managed = False
        db_table = 'flower'


class Goods(models.Model):
    goods_id = models.AutoField(primary_key=True, db_comment='商品编号')
    good_sort = models.CharField(max_length=50, blank=True, null=True, db_comment='商品种类')
    gname = models.CharField(max_length=50, blank=True, null=True, db_comment='商品名称')
    flower_id = models.CharField(max_length=50, blank=True, null=True, db_comment='花编号')
    image = models.CharField(max_length=255, blank=True, null=True, db_comment='商品图片')
    ename = models.CharField(max_length=255, blank=True, null=True, db_comment='英文名')
    size = models.CharField(max_length=50, blank=True, null=True, db_comment='尺寸')
    charge = models.CharField(max_length=50, blank=True, null=True, db_comment='价格')
    total_num = models.CharField(max_length=50, blank=True, null=True, db_comment='总数')
    stage = models.CharField(max_length=50, blank=True, null=True, db_comment='库存状态')
    salenum = models.IntegerField(max_length=50, blank=True, null=True, db_comment='销售量')

    class Meta:
        managed = False
        db_table = 'goods'


class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True, db_comment='管理员编号')
    mname = models.CharField(max_length=50, blank=True, null=True, db_comment='管理员名字')
    phone = models.CharField(max_length=50, blank=True, null=True, db_comment='联系方式')
    password = models.CharField(max_length=50, blank=True, null=True, db_comment='密码')
    photo = models.CharField(max_length=255, blank=True, null=True, db_comment='照片')
    days = models.CharField(max_length=10, blank=True, null=True, db_comment='到店天数')
    address = models.CharField(max_length=50, blank=True, null=True, db_comment='现居地')
    restrict = models.CharField(max_length=50, blank=True, null=True, db_comment='权限')
    sex = models.CharField(max_length=50, blank=True, null=True, db_comment='性别')
    age = models.CharField(max_length=50, blank=True, null=True, db_comment='年龄')
    stage = models.CharField(max_length=50, blank=True, null=True, db_comment='状态')
    date = models.DateField(blank=True, null=True, db_comment='入职日期')

    class Meta:
        managed = False
        db_table = 'manager'


class Operate(models.Model):
    op_id = models.AutoField(primary_key=True, db_comment='操作编号')
    op_name = models.CharField(max_length=50, blank=True, null=True, db_comment='操作内容')
    gname = models.CharField(max_length=50, blank=True, null=True, db_comment='商品名称')
    goods_id = models.CharField(max_length=10, blank=True, null=True, db_comment='商品编号')
    size = models.CharField(max_length=50, blank=True, null=True, db_comment='尺寸')
    op_time = models.DateTimeField(blank=True, null=True, db_comment='操作时间')
    op_num = models.CharField(max_length=50, blank=True, null=True, db_comment='操作数量')
    op_person = models.CharField(max_length=50, blank=True, null=True, db_comment='操作人员')
    op_person_id = models.CharField(max_length=10, blank=True, null=True, db_comment='操作人员编号')
    op_other = models.CharField(max_length=255, blank=True, null=True, db_comment='操作备注')

    class Meta:
        managed = False
        db_table = 'operate'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True, db_comment='订单编号')
    time = models.DateTimeField(blank=True, null=True, db_comment='下单时间')
    stage = models.CharField(max_length=50, blank=True, null=True, db_comment='订单状态')
    address_id = models.CharField(max_length=50, blank=True, null=True, db_comment='收货地址，对应address表的id')
    money = models.CharField(max_length=50, blank=True, null=True, db_comment='金额')
    user_id = models.CharField(max_length=10, blank=True, null=True, db_comment='下单用户编号')
    beihuo = models.CharField(max_length=50, blank=True, null=True, db_comment='备货人员')
    beihuo_id = models.CharField(max_length=10, blank=True, null=True, db_comment='备货人员编号')
    peisong = models.CharField(max_length=50, blank=True, null=True, db_comment='配送人员')
    peisong_id = models.CharField(max_length=10, blank=True, null=True, db_comment='配送人员编号')
    remark = models.CharField(max_length=255, blank=True, null=True, db_comment='评价')
    cart_id = models.CharField(max_length=50, blank=True, null=False, db_comment='cart id')
    aname = models.CharField(max_length=50, blank=True, null=False, db_comment='收货人名字')
    address = models.CharField(max_length=50, blank=True, null=False, db_comment='收货人地址')
    phone = models.CharField(max_length=50, blank=True, null=False, db_comment='收货人手机号')

    class Meta:
        managed = False
        db_table = 'order'


class Sort(models.Model):
    sort_id = models.CharField(max_length=50, db_comment='分类编号')
    tab_id = models.CharField(max_length=50, blank=True, null=True, db_comment='标签编号')
    tab_name = models.CharField(max_length=50, blank=True, null=True, db_comment='标签名称')
    tab = models.CharField(max_length=50, blank=True, null=True, db_comment='分类名称')

    class Meta:
        managed = False
        db_table = 'sort'


class Tool(models.Model):
    tool_id = models.AutoField(primary_key=True, db_comment='工具编号')
    tname = models.CharField(max_length=50, blank=True, null=True, db_comment='名称')
    image = models.CharField(max_length=255, blank=True, null=True, db_comment='图片')
    image2 = models.CharField(max_length=255, blank=True, null=True, db_comment='图片2')
    image3 = models.CharField(max_length=255, blank=True, null=True, db_comment='图片3')
    sort = models.CharField(max_length=50, blank=True, null=True, db_comment='分类')
    num = models.CharField(max_length=50, blank=True, null=True, db_comment='库存')

    class Meta:
        managed = False
        db_table = 'tool'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    photo = models.CharField(max_length=255, blank=True, null=True, db_comment='头像')
    uname = models.CharField(max_length=50, blank=True, null=True, db_comment='用户名')
    keyword = models.CharField(max_length=50, blank=True, null=True, db_comment='密码')
    phone = models.CharField(max_length=50, blank=True, null=True, db_comment='联系方式')
    sex = models.CharField(max_length=10, blank=True, null=True, db_comment='性别')
    age = models.IntegerField(blank=True, null=True, db_comment='年龄')
    address = models.CharField(max_length=255, blank=True, null=True, db_comment='现居地')
    time = models.DateField(blank=True, null=True, db_comment='注册日期')
    postnum = models.CharField(max_length=10, blank=True, null=True, db_comment='邮政编码')
    e_mail = models.CharField(db_column='e-mail', max_length=50, blank=True, null=True,
                              db_comment='邮箱')  # Field renamed to remove unsuitable characters.
    intor = models.CharField(max_length=255, blank=True, null=True, db_comment='个签')
    stage = models.CharField(max_length=50, blank=True, null=True, db_comment='用户等级')

    class Meta:
        managed = False
        db_table = 'user'


class Likes(models.Model):
    like_id = models.AutoField(primary_key=True, db_comment='主键，唯一id')
    user_id = models.IntegerField(db_comment='用户')
    flower_id = models.IntegerField(db_comment='用户喜欢的一朵花的id')
    image = models.CharField(max_length=255, blank=True, null=True, db_comment='花的图片')
    price = models.IntegerField(blank=True, null=True, db_comment='该花最小号的价格')

    class Meta:
        managed = False
        db_table = 'likes'


class Msg(models.Model):
    msgid = models.AutoField(db_column='msgId', primary_key=True, db_comment='消息id')  # Field name made lowercase.
    chatid = models.IntegerField(db_column='chatId', blank=True, null=True, db_comment='会话id')  # Field name made lowercase.
    userid = models.CharField(db_column='userId', max_length=20, blank=True, null=True, db_comment='用户id')  # Field name made lowercase.
    userpro = models.CharField(db_column='userPro', max_length=10, blank=True, null=True, db_comment='用户属性')  # Field name made lowercase.
    creattime = models.TimeField(db_column='creatTime', blank=True, null=True, db_comment='创建时间')  # Field name made lowercase.
    chatmsg = models.CharField(db_column='chatMsg', max_length=255, blank=True, null=True, db_comment='消息内容')  # Field name made lowercase.
    readstate = models.CharField(db_column='readState', max_length=10, blank=True, null=True, db_comment='查看状态，0未读，1已读')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'msg'


class Chat(models.Model):
    chatid = models.AutoField(db_column='chatId', primary_key=True, db_comment='会话id')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True, db_comment='用户id')  # Field name made lowercase.
    chattime = models.DateField(db_column='chatTime', blank=True, null=True, db_comment='会话创建时间')  # Field name made lowercase.
    chatstate = models.CharField(db_column='chatState', max_length=10, blank=True, null=True, db_comment='会话状态，0正在进行，1已结束')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chat'
