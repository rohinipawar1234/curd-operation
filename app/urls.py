from django.urls import path
from app.views import*

urlpatterns = [
    path("",Index),
    path('registerdata',Register,name='registerdata'),
    path('showdata',Showdata,name='showdata'),
    path('updatepage/<int:id>',Update,name='updatepage'),
    path('deletedata/<int:id>',Deletedata,name='deletedata'),
    path('editpage/<int:pk>',Editpage,name='editpage'),
]
