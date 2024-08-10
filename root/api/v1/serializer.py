from rest_framework import serializers
from root.models import *


class SpecialServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialServices
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class TeamMainSerilizer(serializers.ModelSerializer):
    class Meta:
        model = TeamMain
        fields = '__all__'