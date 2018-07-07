
from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$',FetchVotingResult),
    url(r'^vote$',VoteRequest),
    url(r'^locations$',LocationsDetail),
    url(r'^api/$',VoteListAPIView.as_view()),
    url(r'^api/location$',LocationListCreateAPIView.as_view()),
    url(r'^api/vote$',VoteLogListCreateAPIView.as_view()),
]
