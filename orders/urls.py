#!/user/bin/env python3
# -*- coding: utf-8 -*-


from django.urls import path

from orders.views import OrdersToDoNum, OrdersToDeliverNum
from users.views import ShowUsersInfo, ShowNewUsersToday

urlpatterns = [
    path('toPrepareNum/', OrdersToDoNum.as_view()),
    path('toDeliverNum/', OrdersToDeliverNum.as_view()),
]
