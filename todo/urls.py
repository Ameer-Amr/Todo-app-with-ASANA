from django.urls import path
from .views import TodoApiView, TodoApiDeleteView

urlpatterns = [
    path('', TodoApiView.as_view(), name="todoAPI"),
    path('api/delete/<str:gid>', TodoApiDeleteView.as_view(), name="todoAPI"),
]