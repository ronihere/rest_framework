from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Company
from api.serializers import CompanySerializer

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls= {
        'List': '/company-list/',
        'Detail View':'/company-detail/<str:pk>/',
        'Create':'/company-create/',
        'Update':'/company-update/<str:pk>/',
        'Delete':'/company-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def companyList(request):
    company = Company.objects.all()
    serializer = CompanySerializer(company, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def companyDetail(request,id):
    company = Company.objects.get(company_id=id)
    serializer = CompanySerializer(company, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def companyCreate(request):
    serializer = CompanySerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['POST'])
def companyUpdate(request,id):
    company = Company.objects.get(company_id=id)
    serializer = CompanySerializer(instance = company , data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def companyDelete(request,id):
    
    company = Company.objects.get(company_id=id)
    serializer = CompanySerializer(company)
    company.delete()
    
    return Response({'message':'successfully deleted'})    


    
