from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add', views.add, name='add'),
    path('success', views.success, name="success"),
    path('edit', views.edit, name='edit'),
    path('submit', views.submit),
    path('delete', views.delete)
]
