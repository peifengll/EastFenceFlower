from django.urls import path

from manager.views import ShowAllManagersInfo, ManagerAddView, ManagerDelView, ManagerUpdateView

urlpatterns = [
    path('managers/show', ShowAllManagersInfo.as_view()),
    path('managers/add', ManagerAddView.as_view()),
    path('managers/del', ManagerDelView.as_view()),
    path('managers/update', ManagerUpdateView.as_view()),
]
