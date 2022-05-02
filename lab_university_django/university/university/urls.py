from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index_render', views.index_render),
    path('universityInfo', views.university_info),
    path('disciplineInfo', views.discipline_info),
    path('departmentsInfo', views.department_info),
    path('groupsInfo', views.groups_info),
    path('universityStructureInfo', views.university_structure)
]

# end
# 2022-05-02
# Created: https://github.com/alwayswanna
