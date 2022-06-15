from django.contrib import admin
from django.urls import path, include
#from main.views import viewpic
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),     
    path('', include('prayers.urls')),
    path('monks/', include('main.urls')),
    #path('pics/<int:pictura_id>', viewpic)
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
