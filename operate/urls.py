from django.urls import path

from operate.views import OperateUpdateView, OperateAddView, OperateShowView

urlpatterns = [
    path('operate/update', OperateUpdateView.as_view()),
    path('operate/add', OperateAddView.as_view()),
    path('operate/show', OperateShowView.as_view()),
]
