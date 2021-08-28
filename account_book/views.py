from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import account_book.service.main_account_book_service as main_account_book_service
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
