from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('division_list', views.DivisionList.as_view()),
    path('member_list', views.MemberList.as_view()),
    path('payment_list/<str:member_id>', views.PaymentList.as_view()),
    path('category_list/<str:division_id>', views.CategoryListByDivisionId.as_view()),
    path('category_seq_list/<str:category_id>', views.CategorySeqList.as_view()),
    path('account', views.Account.as_view()),
    path('category_sum/<str:division_id>', views.CategorySum.as_view()),
    path('category_seq_sum/<str:division_id>', views.CategorySeqSum.as_view()),
    path('division_sum', views.DivisionSum.as_view()),
    path('member_sum', views.MemberSum.as_view()),
    path('fixed_price_sum', views.FixedPriceSum.as_view()),
    path('division_sum_daily', views.DivisionSumDaily.as_view()),
    path('expense_sum_daily', views.ExpenseSumDaily.as_view()),
    path('my_asset_list', views.MyAssetList.as_view())
]