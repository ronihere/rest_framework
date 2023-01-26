#create serializers here
from api.models import Company
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
    
    def validate(self, data):
        if data['active']==False:
            raise serializers.ValidationError({'error':"Organisation can't be inactive"})
        if data['Name']:
            for i in data['Name']:
                if i.isdigit():
                    raise serializers.ValidationError({'error':'Name can not contain any numbers(0-9)'})
        return data