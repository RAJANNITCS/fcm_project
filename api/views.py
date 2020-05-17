from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from myapp.models import Token



class save_token(APIView):
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        if token:
            Token(token=token)
            data = Token(token=token)
            data.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


