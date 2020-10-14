from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^api/users/$', UsersView.as_view()),
    url(r'^login/$', Login.as_view()),
    url(r'^api/borrow/books/$', BorrowBook.as_view()),
    url(r'^api/tokens/$', Tokens.as_view()),





]
