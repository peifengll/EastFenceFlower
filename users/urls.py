#!/user/bin/env python3
# -*- coding: utf-8 -*-


from django.urls import path
from libs.utils.jwtSerializer import MyTokenObtainPairView
from users.views import ShowUsersInfo, ShowNewUsersToday, ShowNewUsersTodayNum, UserSearch

urlpatterns = [
    path('userlist/', ShowUsersInfo.as_view()),
    path('newuserlist/', ShowNewUsersToday.as_view()),
    path('newUsersNum/', ShowNewUsersTodayNum.as_view()),
    path('userSearch/', UserSearch.as_view()),

]
