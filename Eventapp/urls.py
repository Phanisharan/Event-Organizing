from django.urls import path
from .views import *
from admin_role.views import *

app_name = 'Eventapp'

urlpatterns = [
    path('', home, name='home'),
    path('gallery/', gallery, name='gallery'),
    path('venue/', venue, name='venue'),
    path('planningservice/', planningservices, name='planning-services'),
    path('viewdetail/<int:id>/', viewdetail, name='viewdetail'),
    path('wedding_gallery/<int:id>/', wedding_gallery, name='wedding_gallery'),
    path('contact/', contact, name='contact'),
    path('thankyou/', thankyou, name='thankyou'),
    path('custom_admin/', custom_admin, name='custom_admin'),
    path('records_page/', records_page, name='records_page'),
    path('tracked_info/', tracked_info, name='tracked_info'),
    path('custom_admin/edit/<str:model>/<int:id>/', edit_record, name='edit_record'),
    path('custom_admin/delete/<str:model>/<int:id>/', delete_record, name='delete_record'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]