from .models import *
from rest_framework.serializers import ModelSerializer, StringRelatedField
from datetime import datetime
                      
                            
class LocationSerializer(ModelSerializer):
    class Meta:
        model= Location
        fields=[
            'name',
            'location_address',
            'number_of_dustbin',
        ]

class VoteSerializer(ModelSerializer):
    class Meta:
        model= Vote
        fields=[
            'location',
            'date',
            'votes',
            'updated_at',
            
        ]
        depth = 1
            
class VoteLogSerializer(ModelSerializer):
    class Meta: 
        model=VoteLog
        fields=[
            'location',
            'voted',
            'created_date',
        ]
        
    def create(self, validated_data):
        loc=validated_data['location']
        voted=validated_data['voted']
        loc_obj=Vote.objects.filter(location=loc,date=datetime.today())
        if loc_obj.exists():
            loc_obj=loc_obj[0]
        else:
            loc_obj=Vote.objects.create(location=loc,date=datetime.today())
            loc_obj.save()
            
        if voted:
            loc_obj.votes+=1
        else:
            loc_obj.votes-=1
        loc_obj.save()
        vote_log_obj=VoteLog(location=loc,voted=voted)
        vote_log_obj.save()
        return validated_data
            