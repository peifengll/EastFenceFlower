#!/user/bin/env python3
# -*- coding: utf-8 -*-


from django.urls import path

from goods.views import GoodsAllInfo, GoodsOneInfoById, GoodsDeleteById, GoodsFirstThree, GoodsAdd, GoodsUpdate, \
    GoodsInfoSearch
from orders.views import OrdersToDoNum, OrdersToDeliverNum, OrdersShowAll
from users.views import ShowUsersInfo, ShowNewUsersToday

urlpatterns = [
    path('goods/allinfo', GoodsAllInfo.as_view()),
    path('goods/detail', GoodsOneInfoById.as_view()),
    path('goods/del', GoodsDeleteById.as_view()),
    path('goods/three', GoodsFirstThree.as_view()),
    path('goods/add', GoodsAdd.as_view()),
    path('goods/update', GoodsUpdate.as_view()),
    path('goods/search', GoodsInfoSearch.as_view()),

]
