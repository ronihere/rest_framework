from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api import views





urlpatterns = [
    path('',views.apiOverview,name ='apiOverview'),
    path('company-list/',views.companyList, name='companyList'),
    path('company-detail/<str:id>/',views.companyDetail, name='companyDetail'),
    path('company-create/',views.companyCreate, name='companyCreate'),
    path('company-update/<str:id>/',views.companyUpdate, name='companyUpdate'),
    path('company-delete/<str:id>/',views.companyDelete, name='companyDelete'),
    
    # path('api-auth/', include('rest_framework.urls'))
]