from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .feeds import LastedPostFeed
app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('test/', views.tests, name='test'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    # SEO-friendly
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('feed/', LastedPostFeed(), name='post_feed')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
