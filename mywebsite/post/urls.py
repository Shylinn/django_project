from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,HomePostListView,UserUpdateView
from django.contrib.auth.views import LoginView
from .views import LogoutView


from . import views
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('',HomePostListView.as_view(),name="index"),
    path('about/',views.about,name="about"),
    path('services/',views.services,name="services"),
    path('posts/list', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', PostListView.as_view(template_name='index.html'), name='index'),
    path('profile/<int:pk>', UserUpdateView.as_view(), name='profile'),
   

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)