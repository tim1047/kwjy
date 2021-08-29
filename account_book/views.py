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


class AccountList(APIView):
    def get(self, request):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            result_data = main_account_book_service.get_main_list()
        except Exception as e:
            result_message = 'FAIL'
            result_data = {}
            exc_info = sys.exc_info()
            error_message = ''.join(traceback.format_exception(*exc_info))
        return Response({'result_message': result_message, 'result_data': result_data, 'error_message': error_message})

    def post(self, request):
        return Response({'result_message': 'SUCCESS'})

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

class CategoryListByDivisionId(APIView):
    def get(self, request, division_id):
        result_message = 'SUCCESS'
        result_data = dict()
        error_message = None

        try:
            param = {
                'division_id': int(division_id)
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