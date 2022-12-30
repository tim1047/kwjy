from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('division', views.DivisionList.as_view()),
    path('division/<str:division_id>/category', views.CategoryListByDivisionId.as_view()),
    path('division/<str:division_id>/category/sum', views.CategorySum.as_view()),
    path('division/<str:division_id>/category_seq/sum', views.CategorySeqSum.as_view()),
    path('division/<str:division_id>/sum', views.DivisionSumByDivisionId.as_view()),
    path('division/sum', views.DivisionSum.as_view()),
    path('division/sum/daily', views.DivisionSumDaily.as_view()),
    path('member', views.MemberList.as_view()),
    path('member/<str:member_id>/payment', views.PaymentList.as_view()),
    path('member/sum', views.MemberSum.as_view()),
    path('category/<str:category_id>/category_seq', views.CategorySeqList.as_view()),
    path('account', views.Account.as_view()),
    path('fixed_price/sum', views.FixedPriceSum.as_view()),
    path('expense/sum/daily', views.ExpenseSumDaily.as_view()),
    path('asset', views.AssetList.as_view()),
    path('my_asset', views.MyAsset.as_view()),
    path('my_asset/accum', views.MyAssetAccum.as_view()),
]