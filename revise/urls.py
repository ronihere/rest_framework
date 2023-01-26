from revise import views
from django.urls import path

urlpatterns = [
    path('stu-reg/',views.stu_reg , name ='stu_reg'),
]


