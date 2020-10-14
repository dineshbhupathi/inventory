from django.shortcuts import render,redirect
from rest_framework.generics import *
from .serializers import *
from .models import *
from django.contrib.auth import login, authenticate,logout
from rest_framework.response import Response
import json
import requests
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


# url = 'http://127.0.0.1:8000/api/borrow/books/'
# headers = {'Authorization': 'Token 9054f7aa9305e012b3c2300408c3dfdf390fcddf'}
# r = requests.get(url, headers=headers)

class UsersView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class Login(views.APIView):
    def post(self, request):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")
        username = request.data['email']
        password = request.data['password']
        try:
            user = authenticate(username=username, password=password)
        except User.DoesNotExist:
            return Response({'Error': "Invalid email/password"}, status="400")
        if user:
            login(request, user)
            return redirect("/api/borrow/books/")
        else:
            return Response(
                json.dumps({'Error': "Invalid credentials"}),
                status=404,
                content_type="application/json"
            )
class BorrowBook(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BorrowBookSerializer
    queryset = BorrowBook.objects.all()

    def post(self, request, *args, **kwargs):
        # taking quanttiy
        quantity = request.data['quantity']
        # taking product object id
        book_id = request.data['book']
        # with product id filtering product object
        books_queryset = Books.objects.filter(id=book_id).values('book_count')
        for book in books_queryset:
            update_count = book['book_count'] - int(quantity)
            print(update_count, 'lll')
            # updating product qunatity
            Books.objects.filter(id=book_id).update(book_count=update_count)
        return self.create(request, *args, **kwargs)

class Tokens(ListAPIView):
    serializer_class = TokenSerializer
    queryset = Token.objects.all()