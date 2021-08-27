from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
def index(request):
    return render(request, 'index.html')


class Test(APIView):
    def get(self, request):
        return Response({'resultMessage': 'OK'})

    def post(self, request):
        return Response({'resultMessage': 'OK'})
