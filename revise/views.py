from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentRegistration
# Create your views here.

def stu_reg(request):
    form = StudentRegistration()
    return render(request , 'revise/stu_reg.html',{'form':form})
