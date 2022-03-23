from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import account_book.service.main_account_book_service as main_account_book_service
import account_book.service.insert_account_service as insert_account_service
import sys
import traceback


# Create your views here.
def index(request):
    return render(request, 'index.html')

class DivisionList(APIView):
    def get(self, request):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            result_data = insert_account_service.get_division_list()
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

    def post(self, request):
        return Response({'result_message': 'SUCCESS'})

class MemberList(APIView):
    def get(self, request):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            result_data = insert_account_service.get_member_list()
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

    def post(self, request):
        return Response({'result_message': 'SUCCESS'})

class PaymentList(APIView):
    def get(self, request, member_id):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            param = {
                'member_id': member_id
            }
            result_data = insert_account_service.get_payment_list(param)
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

    def post(self, request):
        return Response({'result_message': 'SUCCESS'})

class CategoryListByDivisionId(APIView):
    def get(self, request, division_id):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            param = {
                'division_id': division_id
            }
            result_data = insert_account_service.get_category_list_by_division_id(param)
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

    def post(self, request):
        return Response({'result_message': 'SUCCESS'})

class CategorySeqList(APIView):
    def get(self, request, category_id):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            param = {
                'category_id': category_id
            }
            result_data = insert_account_service.get_category_seq_list(param)
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

    def post(self, request):
        return Response({'result_message': 'SUCCESS'})

class Account(APIView):
    def get(self, request):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            request_data = request.GET
            param = {
                'strt_dt': request_data.get('strtDt', ''),
                'end_dt': request_data.get('endDt', '')
            }
            result_data = main_account_book_service.get_main_list(param)
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

    def post(self, request):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            insert_account_service.insert_account(request.data)
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})
    
    def put(self, request):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            insert_account_service.update_account(request.data)
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

    def delete(self, request):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            insert_account_service.delete_account(request.data)
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

class CategorySum(APIView):
    def get(self, request, division_id):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            param = {
                'division_id': division_id
            }

            request_data = request.GET
            if request_data:
                param['strt_dt'] = request_data.get('strtDt', '')
                param['end_dt'] = request_data.get('endDt', '')

            result_data = main_account_book_service.get_category_sum(param)
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

    def post(self, request):
        return Response({'result_message': 'SUCCESS'})

class CategorySeqSum(APIView):
    def get(self, request, division_id):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            param = {
                'division_id': division_id
            }

            request_data = request.GET
            if request_data:
                param['strt_dt'] = request_data.get('strtDt', '')
                param['end_dt'] = request_data.get('endDt', '')
                
            result_data = main_account_book_service.get_category_seq_sum(param)
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

    def post(self, request):
        return Response({'result_message': 'SUCCESS'})

class DivisionSum(APIView):
    def get(self, request):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            request_data = request.GET
            param = {
                'strt_dt': request_data.get('strtDt', ''),
                'end_dt': request_data.get('endDt', '')
            }
            result_data = main_account_book_service.get_division_sum(param)
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

    def post(self, request):
        return Response({'result_message': 'SUCCESS'})

class MemberSum(APIView):
    def get(self, request):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            request_data = request.GET
            param = {
                'strt_dt': request_data.get('strtDt', ''),
                'end_dt': request_data.get('endDt', '')
            }
            result_data = main_account_book_service.get_member_sum(param)
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

    def post(self, request):
        return Response({'result_message': 'SUCCESS'})

class FixedPriceSum(APIView):
    def get(self, request):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            request_data = request.GET
            param = {
                'strt_dt': request_data.get('strtDt', ''),
                'end_dt': request_data.get('endDt', '')
            }
            result_data = main_account_book_service.get_fixed_price_sum(param)
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

    def post(self, request):
        return Response({'result_message': 'SUCCESS'})

class DivisionSumDaily(APIView):
    def get(self, request):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            request_data = request.GET
            param = {
                'strt_dt': request_data.get('strtDt', ''),
                'end_dt': request_data.get('endDt', '')
            }
            result_data = main_account_book_service.get_division_sum_daily(param)
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

    def post(self, request):
        return Response({'result_message': 'SUCCESS'})

    
class ExpenseSumDaily(APIView):
    def get(self, request):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            request_data = request.GET
            param = {
                'strt_dt': request_data.get('strtDt', ''),
                'end_dt': request_data.get('endDt', '')
            }
            result_data = main_account_book_service.get_expense_sum_daily(param)
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

    def post(self, request):
        return Response({'result_message': 'SUCCESS'})

class MyAssetList(APIView):
    def get(self, request):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            request_data = request.GET
            param = {
                'strt_dt': request_data.get('strtDt', ''),
                'end_dt': request_data.get('endDt', '')
            }
            result_data = main_account_book_service.get_my_asset_list(param)
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
            print(''.join(traceback.format_exception(*exc_info)))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

    def post(self, request):
        return Response({'result_message': 'SUCCESS'})


class AssetList(APIView):
    def get(self, request):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            result_data = main_account_book_service.get_asset_list()
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

    def post(self, request):
        return Response({'result_message': 'SUCCESS'})


class MyAsset(APIView):
    def post(self, request):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            result_data = main_account_book_service.insert_my_asset(request.data)
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

    def get(self, request):
        return Response({'result_message': 'SUCCESS'})

    def put(self, request):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            result_data = main_account_book_service.update_my_asset(request.data)
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})
        