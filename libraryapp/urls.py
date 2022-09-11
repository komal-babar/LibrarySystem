from django.urls import URLPattern,path
from .views import Bookview

urlpatterns=[
    path('books/', Bookview.as_view()),
    path('books/<int:id>',Bookview.as_view()),

 ]