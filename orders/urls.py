#!/user/bin/env python3
# -*- coding: utf-8 -*-


from django.urls import path

from orders.views import OrdersToDoNum, OrdersToDeliverNum, OrdersShowAll, OrdersSearch, OrdersDel, OrdersUpdate, \
    OrderProfitView
from users.views import ShowUsersInfo, ShowNewUsersToday

urlpatterns = [
    path('toPrepareNum/', OrdersToDoNum.as_view()),
    path('toDeliverNum/', OrdersToDeliverNum.as_view()),
    path('order/allinfo/', OrdersShowAll.as_view()),
    path('order/search', OrdersSearch.as_view()),
    path('order/update', OrdersUpdate.as_view()),
    path('order/del', OrdersDel.as_view()),
    path('order/profit', OrderProfitView.as_view()),
]
