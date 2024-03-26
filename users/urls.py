#!/user/bin/env python3
# -*- coding: utf-8 -*-


from django.urls import path
from libs.utils.jwtSerializer import MyTokenObtainPairView
from users.views import ShowUsersInfo, ShowNewUsersToday, ShowNewUsersTodayNum, UserSearch, GetUsersPageTotal, UserAll, \
    UserDetail, UserDel, UserFirstThree, UserAdd, UserUpdate, UserSearchView

urlpatterns = [
    path('userlist/', ShowUsersInfo.as_view()),
    path('newuserlist/', ShowNewUsersToday.as_view()),
    path('newUsersNum/', ShowNewUsersTodayNum.as_view()),
    path('userSearch/', UserSearch.as_view()),
    path('userpagenum/', GetUsersPageTotal.as_view()),
    path('user/allinfo', UserAll.as_view()),
    path('user/search', UserSearchView.as_view()),
    path('user/detail', UserDetail.as_view()),
    path('user/del', UserDel.as_view()),
    path('user/three', UserFirstThree.as_view()),
    path('user/add', UserAdd.as_view()),
    path('user/update', UserUpdate.as_view()),

]
