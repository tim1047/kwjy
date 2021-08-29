from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('account_list', views.AccountList.as_view()),
    path('division_list', views.DivisionList.as_view())
]