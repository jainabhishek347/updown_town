from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static

#from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title='Upside Down API')
from . import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('profiles.urls')),
    #url(r'^api/doc', get_swagger_view(title='Rest API Document')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
