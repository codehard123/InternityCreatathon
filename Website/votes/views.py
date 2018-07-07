from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import(
    RetrieveUpdateAPIView,
    ListCreateAPIView,
    ListAPIView
)

from rest_framework.permissions import(
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)

#class PostVoteView(APIView):
#    """
#    Update the voting
#    """
#
#    def post(self, request, format=None):
#        serializer = SnippetSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#    
#       'name',
#            'date',
#            'votes',
#            'updated_at',
class VoteLogListCreateAPIView(ListCreateAPIView):
    queryset = VoteLog.objects.all()
    serializer_class = VoteLogSerializer
    permission_classes= [AllowAny]

class LocationListCreateAPIView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
    
class VoteListAPIView(ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes= [AllowAny]
    
def FetchVotingResult(request):

    votes=Vote.objects.order_by('-date')
    return render(request,"home.html",{
    
        "votes":votes,
    })

def VoteRequest(request):
    locations=Location.objects.all()
    return render(request,"vote.html",{
        "locations":locations,
    })

def LocationsDetail(request):
    locations=Location.objects.all()
    return render(request,"locations.html",{
        "locations":locations,
    })
    