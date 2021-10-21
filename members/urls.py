from django.urls import path
from .views import MemberUpdateView, landing_view, member_detail, member_update, new_member, member_list, MembersDetailView

app_name = 'members'

urlpatterns = [
    path('', landing_view, name='landing'),
    path('members/', member_list, name='mem-list'),
    path('create/', new_member, name='mem-create'),
    path('members/<int:pk>/', member_detail, name='mem-detail'),
    path('members/<int:pk>/update/', member_update , name='mem-update')
    ]