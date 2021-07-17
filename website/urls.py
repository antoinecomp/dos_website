from django.contrib import admin
from django.urls import path, include
from dos_website import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', views.home, name='home'),

    # blog
    path('blog/', include('blog.urls')),

    # productions
    path('productions/', views.productions, name='productions'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
