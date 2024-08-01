from django.urls import path
from .views import *

app_name = 'collab'

urlpatterns = [
    path('all-clubs/', ListClubsView.as_view(), name='all_clubs'),
    path('create-club/', CreateClubView.as_view(), name='create_club'),
    path('profile-user/', ProfileUser.as_view(), name='profile_user'),
    path('detail-club/<slug:slug>/', DetailClubView.as_view(), name='detail_club'),
    path('join-club/<slug:slug>/', join_club_view, name='join_club'),
    path('send-msg/<slug:slug>/<int:pk>/', SendMsgView.as_view(), name='send_msg'),
    # for author club only
    path('list-confirm-team/<slug:slug>/', ListRequestTeamView.as_view(), name='list_confirm_team'),
]