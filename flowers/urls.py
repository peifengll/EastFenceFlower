#!/user/bin/env python3
# -*- coding: utf-8 -*-


from django.urls import path

from flowers.views import FlowerInfoSearch, FlowerAdd, FlowerUpdate, FlowerDel, UploadImageView
from orders.views import OrdersToDoNum, OrdersToDeliverNum, OrdersShowAll
from users.views import ShowUsersInfo, ShowNewUsersToday

urlpatterns = [
    path('flower/search', FlowerInfoSearch.as_view()),
    path('flower/add', FlowerAdd.as_view()),
    path('flower/update', FlowerUpdate.as_view()),
    path('flower/del', FlowerDel.as_view()),
    path('flower/upload', UploadImageView.as_view()),
]
