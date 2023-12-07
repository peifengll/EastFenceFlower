import uuid

from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class TestView(APIView):

    def post(self, request, *args, **kwargs):
        s = str(request.user.__dict__)
        return Response(data=s)
