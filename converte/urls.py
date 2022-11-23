from django.urls import path
from . import views
urlpatterns=[
    path('',views.retornaHtml,name='retornaHtml'),
    path('ctv/',views.ctv,name='ctv'),
    path('cvt/',views.cvt,name='cvt'),
]
