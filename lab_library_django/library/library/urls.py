from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lib_site.urls')),
]

# end
# Created: https://github.com/alwayswanna
