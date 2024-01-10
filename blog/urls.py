from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
