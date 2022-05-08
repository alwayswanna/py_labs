from django.urls import path

from . import views

urlpatterns = [
    path('', views.ModuleListView.as_view(), name='main'),
    path('module/<int:pk>', views.more_about_module),
    path('book/<int:pk>', views.more_about_book),
]
