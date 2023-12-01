from . import views
from django.urls import path
from .views import memberList, user_profile


urlpatterns = [    
    # path('', memberList, name='member'),
    
    path('profile/<str:encode_name>/', user_profile, name='user_profile'),
    # path('display_image/', display_image, name='display_image'),
    
    # path('member_list', views.memberList, name='member_list'),
    path('member_create', views.memberCreate, name='member_create'),
    # path('member_update', views.memberUpdate, name='member_update'),
    # path('member_delete', views.memberDelete, name='member_delete')
]
