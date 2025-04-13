from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('apps.blog.urls')),
    path('accounts/',include('apps.user.urls'))
]
