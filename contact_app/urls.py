from django.urls import path
from . import views

app_name = 'contact_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('names/',views.names, name='names'),
    path('names/<int:name_id>/',views.name, name='name'),
    path('new_name/',views.new_name, name='new_name'),
    path('info/',views.info,name='info'),
    path('new_email/<int:name_id>/',views.new_email, name='new_email'),
    path('new_pnum/<int:name_id>/',views.new_pnum,name='new_pnum'),
    path('scode/',views.scode,name='scode'),
]