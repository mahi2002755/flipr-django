from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-panel/add-project/', views.add_project, name='add_project'),
    path('admin-panel/add-client/', views.add_client, name='add_client'),
]